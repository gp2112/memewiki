from flask import Flask
from memewiki.routes import home_bp

__version__ = '0.0.1'

app = Flask(__name__)
app.register_blueprint(home_bp)

if __name__ == '__main__':
    app.run()

