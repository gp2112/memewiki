from flask import Blueprint
from memewiki.controller import login

login_bp = Blueprint('login_bp', __name__)

login_bp.get('/')(login.login)
