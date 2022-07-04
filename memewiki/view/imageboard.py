from flask import render_template
from memewiki.security import captcha

def index(threads: list, username: str=None):
    return render_template('imageboard/index.html', threads=threads, username=username)

def thread(thread, username=None):
    
    comments = thread.getComments()

    return render_template('imageboard/thread.html', 
                                replies=comments, title=thread.titulo,
                                author=thread.usuario.nome, image=thread.midia.url,
                                username=username, descricao=thread.desc, id=thread.id
            )

def create(error: int=0, username: str=None):
    img_cap = captcha.Captcha(n=7, width=280, height=80)
    img_cap.genText()

    captcha.captchas_activated[img_cap.id] = img_cap

    return render_template('imageboard/create.html', captcha=img_cap, error=error, username=username)

