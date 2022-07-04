from flask import Blueprint
from memewiki.controller import meme

memes_bp = Blueprint('memes_bp', __name__)

memes_bp.get('/')(meme.memes)

