from flask import Flask
from memewiki.routes.home_bp import home_bp
from memewiki.routes.imageboard_bp import imageboard_bp

__version__ = '0.0.1'

app = Flask(__name__)
app.register_blueprint(home_bp)
app.register_blueprint(imageboard_bp, url_prefix='/imageboard')

if __name__ == '__main__':
    app.run(debug=True)

