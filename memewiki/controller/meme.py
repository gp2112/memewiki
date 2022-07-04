from flask import session, request, redirect
from memewiki.services import midia as midiaService
from memewiki.services import meme as memeService 
from memewiki.view import meme as memeView
from memewiki.services import memebase as memebaseService
from memewiki.security import captcha

def meme():
    meme_id = request.args.get('id')
    created = request.args.get('success', 0)

    if not meme_id:
        return redirect('/notfound')

    
    try:
        meme_ = memeService.getMeme(meme_id)
    except Exception as e:
        print(e)
        return redirect('/notfound')
    

    return memeView.meme(meme_, username=session.get('username'), created=int(created))

def memes():
    memes = memeService.getLastMemes()
    memesbase = memebaseService.getLastMemesbase()
    return memeView.memes(memes, memesbase, username=session.get('username'))

def create():

    try:
        captcha.captchaControl(request.form)
    except captcha.CaptchaException:
        return redirect('/memes?error=7')

    username = session.get('username')
    if not username:
        return "Você deve estar logado :(", 401

    file = request.files.get('image')
    try:
        midia_id = midiaService.createMidia(file)
    except Exception as e:
        return redirect(request.headers.get('Referer', '/'))

    meme_ = memeService.createMeme(username, midia_id)

    return redirect(f'/meme?id={meme_.id}')


    

