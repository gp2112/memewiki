
from memewiki.models import imageboard
from memewiki.models import user
from memewiki.models import midia

from datetime import datetime



def getThreadsImageBoard(page: int) -> list:

    last_id = imageboard.get_last_threads(1)[0].id

    return imageboard.get_last_threads(50, last_id=last_id - 50*(page-1))

def getThread(id: int) -> imageboard.Thread:
    return imageboard.get_thread(id)


def createThread(title: str, desc: str, username: str, midia_id: int) -> int:
    user_ = user.getUserByName(username)
    if not user_:
        raise Exception('User does not exists!')

    midia_ = midia.getMidia(midia_id) 

    thread = imageboard.Thread(user_, datetime.now(), title, desc, midia_)
    thread.commit()
    return thread.id

"""
def __init__(self, usuario: user.User, idthread: int, 
                    datahora: int, texto: str, midia: midia.Midia):

"""

def createComment(username, thread_id, text, midia_id=None):
    user_ = user.getUserByName(username);
    midia_ = None
    if midia_id:
        midia_ = midia.getMidia(midia_id)
    
    comment = imageboard.ThreadComment(user_, thread_id, datetime.now(), text, midia_) 
    comment.commit()
