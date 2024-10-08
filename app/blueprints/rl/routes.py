from flask import render_template

def register_routes(rl,cache):

    @rl.route('/')
    @cache.cached(timeout=60)
    def index():
        return render_template('rl/index.html')