from flask import session, request, redirect
from memewiki.services import midia as midiaService
from memewiki.services import memebase as memebaseService 
from memewiki.view import memebase as memebaseView
from memewiki.security import captcha


def memebase(title: str):
    
    try:
        memebase_ = memebaseService.getMemebase(title)
    except memebaseService.MemebaseError:
        return f'{title} não encontrado :(', 404
    

    return memebaseView.memebase(memebase_, username=session.get('username'))

def create():
    
    return memebaseView.create(username=session.get('username'))

def createPost():
    username = session.get('username')
    if not username:
        return redirect('/w/create?error=1')
    
    try:
        captcha.captchaControl(request.form)
    except captcha.CaptchaException:
        return redirect('/w/create?error=7')

    titulo = request.form.get('titulo')
    texto = request.form.get('texto')
    
    file = request.files.get('image')

    midia_id = midiaService.createMidia(file)
    memebase_ = memebaseService.createMemeBase(titulo, texto, midia_id, username)

    return redirect(f'/w/{memebase_.titulo}')



