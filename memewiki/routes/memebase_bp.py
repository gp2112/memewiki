from flask import Blueprint
from memewiki.controller import memebase

memebase_bp = Blueprint('memebase_bp', __name__)

memebase_bp.get('/<title>')(memebase.memebase)
memebase_bp.get('/create')(memebase.create)
memebase_bp.post('/create')(memebase.createPost)

