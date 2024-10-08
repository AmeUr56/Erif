from flask import Flask
from flask_caching import Cache

from app import config

cache = Cache()
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    cache.init_app(app)
    
    from .blueprints.main import main
    app.register_blueprint(main,url_prefix='/')

    from .blueprints.regression import regression
    app.register_blueprint(regression,url_prefix='/regression')

    from .blueprints.classification import classification
    app.register_blueprint(classification,url_prefix='/classification')
    
    from .blueprints.cv import cv
    app.register_blueprint(cv,url_prefix='/cv')

    from .blueprints.nlp import nlp
    app.register_blueprint(nlp,url_prefix='/nlp')

    from .blueprints.genai import genai
    app.register_blueprint(genai,url_prefix='/genai')
    
    from .blueprints.ts import ts
    app.register_blueprint(ts,url_prefix='/ts')
    
    from .blueprints.rl import rl
    app.register_blueprint(rl,url_prefix='/rl')
    

    return app