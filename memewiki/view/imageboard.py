from flask import render_template

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

    return render_template('imageboard/create.html', error=error, username=username)

