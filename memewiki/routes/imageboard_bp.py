from flask import Blueprint
from memewiki.controller import imageboard

imageboard_bp = Blueprint('imageboard_bp', __name__)

imageboard_bp.get('/')(imageboard.index)
imageboard_bp.get('/thread/<id>')(imageboard.thread)
imageboard_bp.get('/thread/create')(imageboard.create)
imageboard_bp.post('/thread/create')(imageboard.createPost)
imageboard_bp.post('/thread/<id>/comment')(imageboard.commentPost)
