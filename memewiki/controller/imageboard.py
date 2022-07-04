from flask import request, session, redirect
from memewiki.view import imageboard as imageboardView
from memewiki.services import imageboard as imageboardService
from memewiki.services import midia as midiaService
from memewiki.security import captcha

def index():
     
    page = int(request.args.get('page', 1))

    threads = imageboardService.getThreadsImageBoard(page)
    return imageboardView.index(threads, username=session.get('username')) 

def thread(id: int):
    thread_ = imageboardService.getThread(id)
    return imageboardView.thread(thread_, username=session.get('username'))

def create():
    username = session.get('username')
    if not username:
        return redirect(request.headers.get('Referer', '/'))

    error = int(request.args.get('error', 0))

    return imageboardView.create(username=username, error=error)

def createPost():
    
    try:
        captcha.captchaControl(request.form)
    except captcha.CaptchaException:
        return redirect('/board/thread/create?error=7')

    title = request.form.get('title')
    desc = request.form.get('descricao')
    username = session.get('username')
    if not username:
        return redirect('/login')

    file = request.files.get('image')
    if not file:
        return redirect(request.headers.get('Referer', '/'))
    
    try:
        midia_id = midiaService.createMidia(file)
    except Exception as e:
        print(e)
        return redirect(request.headers.get('Referer', '/'))

    thread_id = imageboardService.createThread(title, desc, username, midia_id)

    return redirect(f'/board/thread/{thread_id}')

def commentPost(id: int):

    username = session.get('username')
    if not username:
        return redirect('/login')

    text = request.form.get('text')
    file = request.files.get('image')

    midia_id = None
    if file:
        midia_id = midiaService.createMidia(file) 

    try:
        imageboardService.createComment(username, id, text, midia_id=midia_id)
    
    except imageboardService.ImageBoardServiceError:
        return redirect(request.url+'?error=1')


    return redirect(f'/board/thread/{id}')

