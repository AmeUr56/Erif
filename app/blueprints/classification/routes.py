from flask import render_template

def register_routes(classification,cache):

    @classification.route('/')
    @cache.cached(timeout=60)
    def index():
        return render_template('classification/index.html')