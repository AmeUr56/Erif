from flask import render_template

def register_routes(main,cache):
    
    @main.route('/')
    @cache.cached(timeout=60)
    def index():
        return render_template('main/index.html')

    @main.route('/models')
    @cache.cached(timeout=60)
    def models():
        return render_template('main/models.html')

    @main.route('/about-us')
    @cache.cached(timeout=60)
    def about_us():
        return render_template('main/about_us.html')