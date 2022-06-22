from flask import render_template

replies = [
            {'author':'user1', 'image':None, 'content':'Hello there'},
            {'author':'user2', 'image':None, 'content':'OMG shit'}
        ]

def thread(name: str):
    
    return render_template('imageboard/thread.html', replies=replies, title=name)

