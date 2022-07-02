from flask import Blueprint
from memewiki.controller import meme

meme_bp = Blueprint('meme_bp', __name__)

meme_bp.get('/')(meme.meme)
meme_bp.post('/create')(meme.create)

