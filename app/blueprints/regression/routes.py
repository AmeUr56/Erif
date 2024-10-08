from flask import render_template

def register_routes(regression,cache):

    @regression.route('/')
    @cache.cached(timeout=60)
    def index():
        return render_template('regression/index.html')