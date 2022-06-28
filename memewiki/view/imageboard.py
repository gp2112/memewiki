from flask import render_template


def thread(title: str, author: str, img: str, replies: list):
    
    return render_template('imageboard/thread.html', styles=['style.css'], 
                                replies=replies, title=title,
                                author=author, image=img
            )

