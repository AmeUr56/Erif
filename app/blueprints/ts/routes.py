from flask import render_template

def register_routes(ts,cache):

    @ts.route('/')
    @cache.cached(timeout=60)
    def index():
        return render_template('ts/index.html')