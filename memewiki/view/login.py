from flask import render_template


def loginPage(error=None, created=None):
    error_msg = None
    if error==1:
        error_msg = 'Você deve preencher o nome de usuário e a senha.'
    elif error==2:
        error_msg = 'Usuário ou senha inválidos!'
    print(error_msg)
    return render_template('login.html', error_msg=error_msg, created=created)


