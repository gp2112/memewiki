from flask import render_template
from memewiki.security import captcha

def memebase(memebase_, username: str=None):
    return render_template('memebase/memesbase.html', memebase=memebase_, 
                    memes=memebase_.getMemes(), username=username, title=memebase_.titulo)

def create(username: str=None):
    cap_img = captcha.Captcha(n=7, width=280, height=80)
    cap_img.genText()

    captcha.captchas_activated[cap_img.id] = cap_img

    return render_template('memebase/create.html', captcha=cap_img, username=username, title="Enviar novo meme base.")
