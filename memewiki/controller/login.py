from flask import request, redirect, session
from memewiki.view import login as loginView
from memewiki.services import user as userService

def login():
    if session.get('username'):
        return redirect('/', 204)

    error = request.args.get('error', 0)
    created = request.args.get('created', 0)

    print(error)
    return loginView.loginPage(error=int(error), created=int(created))

def loginPost():
    nome = request.form.get('username', '')
    senha = request.form.get('password', '')

    if '' in (nome, senha):
        return redirect('/login?error=1', 301)
    if len(senha) < 8:
        return redirect('/login?error=2', 301)

    if not userService.userAuth(nome, senha):
        return redirect('/login?error=2', 301)

    session['username'] = nome

    return redirect('/')

def logout():
    if not session.get('username'):
        return redirect('/', 301)

    session['username'] = None

    return redirect(request.headers.get('Referer', '/'))

