from memewiki.models import midia
from flask import url_for
from hashlib import md5
import os

upload_dir = os.environ.get('MEMEWIKI_UPLOAD_PATH', 'memewiki/static/uploads')

allowed_files = (
        'png', 'jpg', 'gif', 'jpeg', 'webmp', 'webp'
        )

def receiveImg(file) -> str:
    fname = md5(os.urandom(12)+file.filename.encode()).hexdigest()
    extension = file.filename.split('.')[-1].lower()

    if extension not in allowed_files:
        raise Exception('File extension not allowed!')

    fname += '.'+extension

    path = os.path.join(upload_dir, fname)
    file.save(path)
    return fname

def createMidia(file) -> int:
    fname = receiveImg(file)
    midia_ = midia.Midia(None, fname.split('.')[-1], fname)
    midia_.commit()
    return midia_.id



