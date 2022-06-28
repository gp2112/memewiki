from memewiki.view import imageboard

img = 'https://yt3.ggpht.com/a/AGF-l7-24LAwUR3lgvLUVOSTGfDLWYVwtkg1BnLLjA=s900-c-k-c0xffffffff-no-rj-mo'
replies = [
            {'author':'user1', 'image':None, 'content':'Hello there'},
            {'author':'user2', 'image':None, 'content':'OMG shit'}
        ]

title = 'Doge thread, common!!!'

def home():
    return 1

def thread(name: int):
    return imageboard.thread(title, 'guip2112', img, replies)

    
