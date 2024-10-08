from flask import render_template

def register_routes(cv,cache):

    @cv.route('/')
    @cache.cached(timeout=60)
    def index():
        return render_template('cv/index.html')