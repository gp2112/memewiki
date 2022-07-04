from flask import render_template, session



def home():
    return render_template('home.html', title='Bem-vindo à MemeWiki!', 
                                        username=session.get('username'))
