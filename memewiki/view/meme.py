from memewiki.security import captcha
from flask import render_template


def memes(memes: list, memesbase: list, username=None):
    cap_img = captcha.Captcha(n=7, width=280, height=80)
    cap_img.genText()
    captcha.captchas_activated[cap_img.id] = cap_img

    return render_template('memes/memes.html', captcha=cap_img, memes=memes, memesbase=memesbase, username=username)

def meme(meme, username=None, created=0):
    cap_img = captcha.Captcha(n=7, width=280, height=80)
    cap_img.genText()
    captcha.captchas_activated[cap_img.id] = cap_img

    return render_template('memes/meme.html', captcha=cap_img, meme=meme, 
            comments=meme.getComments(), username=username, created=created)
