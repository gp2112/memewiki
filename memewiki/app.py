from flask import Flask
from memewiki.routes.home_bp import home_bp
from memewiki.routes.imageboard_bp import imageboard_bp
from memewiki.routes.login_bp import login_bp
from memewiki.routes.signup_bp import signup_bp
from memewiki.routes.logout_bp import logout_bp
import os

__version__ = '0.0.1'

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(imageboard_bp, url_prefix='/board')
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(signup_bp, url_prefix='/signup')
app.register_blueprint(logout_bp, url_prefix='/logout')

app.secret_key = os.urandom(12)

if __name__ == '__main__':
    app.run(debug=True)

