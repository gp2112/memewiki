from flask import Blueprint
from memewiki.controller import home

home_bp = Blueprint('home_bp', __name__)

home_bp.route('/')(home)
