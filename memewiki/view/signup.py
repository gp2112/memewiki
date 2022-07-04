from flask import render_template
from memewiki.security import captcha

def signupPage(error=0):
    error_msg = None
    if error==1:
       error_msg = 'Você deve preenncher todos os campos'

    elif error==2:
        error_msg = 'E-mail mal formatado.'

    elif error==3:
        error_msg = 'E-mail já cadastrado.'

    elif error==4:
        error_msg = 'Nome de usuário já cadastrado.'

    elif error==5:
        error_msg = 'As senhas não correspondem!'

    elif error==6:
        error_msg = 'A senha deve ter ao menos 8 caracteres.'

    elif error==7:
        error_msg = 'Resposta do captcha incorreta!'

    img_cap = captcha.Captcha(n=7, width=280, height=80)
    img_cap.genText()

    captcha.captchas_activated[img_cap.id] = img_cap

    return render_template('signup.html', captcha=img_cap, error_msg=error_msg)

