from memewiki.models import memebase
from memewiki.models import user
from memewiki.models import midia
from datetime import datetime

class MemebaseError(Exception):

    def __init__(self, msg):
        super().__init__(msg)

def getMemebase(title: str) -> memebase.MemeBase:

    memebase_ = memebase.memebaseByName(title)
    if not memebase_:
        raise MemebaseError('Memebase not found')

    return memebase_

def getLastMemesbase(limit: int=25) -> list:
    memesbase = memebase.getLastMemes(limit)
    return memesbase

def createMemeBase(titulo: str, texto: str, midia_id: int, username: str):

    user_ = user.getUserByName(username)
    midia_ = midia.getMidia(midia_id)

    memebase_ = memebase.MemeBase(None, titulo, midia_, datetime.now(), texto, user_)
    memebase_.commit()
    return memebase_
