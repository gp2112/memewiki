from memewiki.models import meme
from memewiki.models import user
from memewiki.models import midia
from datetime import datetime

def getLastMemes() -> list:
    return meme.getMemes(100)

def getMeme(id: int) -> meme.Meme:
    return meme.getMeme(id)

def createMeme(username: str, midia_id: int) -> meme.Meme:

    user_ = user.getUserByName(username)
    midia_ = midia.getMidia(midia_id)

    meme_ = meme.Meme(None, user_, datetime.now(), midia_, 0, 0)
    meme_.commit()
    return meme_
