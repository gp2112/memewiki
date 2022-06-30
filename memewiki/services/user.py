from memewiki.models import user
from hashlib import sha256
from datetime import datetime

salt = 'wFNHzknZjxeCV6BH1CnuW0wVmO9wzmIHGdLHD2nbsAE='

def userAuth(username: str, password: str) -> bool:
    encript_passwd = sha256((salt+password).encode()).hexdigest()
    user_ = user.getUserByName(username)
    if user_:
        return user_.senha == encript_passwd

    return False

def createUser(username: str, email: str, password: str, birth: int, funcao: str) -> user.User:
    encript_passwd = sha256((salt+password).encode()).hexdigest()
    
    datahoracadastro = datetime.now()

    user_ = user.User(
                None, email, encript_passwd, username, 
                datahoracadastro, datetime.fromtimestamp(birth), funcao
            )
    user_.commit()

    return user_

def getUser(email: str=None, username: str=None) -> user.User:
    if not email and not username:
        raise Exception('email and username empty')

    if email:
        user_ = user.getUserByEmail(email)
        return user_

    if username:
        user_ = user.getUserByName(username)
        return user_

