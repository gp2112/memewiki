from flask import render_template

def memes(memes: list, username=None):

    return render_template('memes/memes.html', memes=memes, username=username)

def meme(meme, username=None, created=0):
    print(meme.__dict__)
    return render_template('memes/meme.html', meme=meme, comments=meme.getComments(), username=username, created=created)
