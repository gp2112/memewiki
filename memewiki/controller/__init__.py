from flask import render_template, session



def home():
    return render_template('home.html', title='Welcome to MemeWiki!', 
                                        username=session.get('username'))
