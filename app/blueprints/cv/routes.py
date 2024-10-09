import os
from flask import render_template,request
from tensorflow.keras.models import load_model
from tensorflow import cast,float32,lite
from PIL import Image
import numpy as np

def register_routes(cv,cache):

    @cv.route('/')
    @cache.cached(timeout=60)
    def index():
        return render_template('cv/index.html')
    
    @cv.route('/gender_recognizer',methods=['GET','POST'])
    def gender_recognizer():
        # Load the TensorFlow Lite model once during startup
        model_path = os.path.join(os.path.dirname(__file__), 'gender_recognizer.tflite')
        interpreter = lite.Interpreter(model_path=model_path)
        interpreter.allocate_tensors()
        
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        
        if request.method == 'POST':
            file = request.files['file']


            img = cast(np.array(Image.open(file.stream).convert('RGB').resize((260,260))),float32)
            img_array = np.expand_dims(img, axis=0)
            
            # Perform inference using the TFLite model
            interpreter.set_tensor(input_details[0]['index'], img_array)
            interpreter.invoke()

            prob = interpreter.get_tensor(output_details[0]['index'])
            pred = round(prob[0][0])

            return render_template('cv/gender_recognizer.html',result=[round(float(prob)*100,2),pred])
        
        return render_template('cv/gender_recognizer.html')