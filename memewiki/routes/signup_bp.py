from flask import Blueprint
from memewiki.controller import signup

signup_bp = Blueprint('signup_bp', __name__)

signup_bp.get('/')(signup.signup)
signup_bp.post('/')(signup.signupPost)
