from memewiki.view import imageboard

def home():
    return 1

def thread(name: str):
    return imageboard.thread(name)

    
