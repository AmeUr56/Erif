from flask import render_template

def register_routes(genai,cache):

    @genai.route('/')
    @cache.cached(timeout=60)
    def index():
        return render_template('genai/index.html')