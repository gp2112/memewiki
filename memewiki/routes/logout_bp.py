from flask import Blueprint
from memewiki.controller import login

logout_bp = Blueprint('logout_bp', __name__)

logout_bp.get('/')(login.logout)
