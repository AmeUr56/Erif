from flask import render_template

def register_routes(nlp,cache):

    @nlp.route('/')
    @cache.cached(timeout=60)
    def index():
        return render_template('nlp/index.html')