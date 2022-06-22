from flask import render_template

def home():
    return 1

def thread(name: str):
    return render_template('imageboard/thread.html', title=name)
