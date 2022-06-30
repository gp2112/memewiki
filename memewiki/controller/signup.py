from flask import request, redirect
from memewiki.view import signup as signupView
from memewiki.services import user as userService
from datetime import datetime
import re

def signup():
    error = request.args.get('error', 0)
    return signupView.signupPage(error=int(error))

def signupPost():
    username = request.form.get('username', '')
    email = request.form.get('email', '')
    senha = request.form.get('password', '')
    senhaRep = request.form.get('passwordrep', '')
    birth = request.form.get('birth', '')

    if '' in (username, email, senha, senhaRep):
        return redirect('/signup?error=1', 301)

    if not re.match(r'[a-z0-9]+@[a-z0-9]+\.[a-z0-9]+', email):
        return redirect('/signup?error=2', 301)
    
    if userService.getUser(email=email):
        return redirect('/signup?error=3', 301)

    if userService.getUser(username=username):
        return redirect('/signup?error=4', 301)

    if senha != senhaRep:
        return redirect('/signup?error=5', 301)

    if len(senha) < 8:
        return redirect('/signup?error=6', 301)

    birth_tmstp = int(datetime.strptime('2011-09-23', '%Y-%m-%d').timestamp())
    usr = userService.createUser(username, email, senha, birth_tmstp, 'comum')
    
    return redirect('/login?created=1', 301)

