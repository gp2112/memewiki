from flask import Blueprint
from memewiki.controller import imageboard

imageboard_bp = Blueprint('imageboard_bp', __name__)

imageboard_bp.get('')(imageboard.home)
imageboard_bp.get('thread/<name>')(imageboard.thread)
