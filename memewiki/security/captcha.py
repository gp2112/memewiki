from captcha.image import ImageCaptcha
from hashlib import sha256
import string
import secrets
import base64
import pathlib
import os


captchas_activated = {}

class CaptchaException(Exception):

    class EmptyCaptcha(Exception):

        def __init__(self):
            super().__init__()
        
        def __str__(self):
            return "Captcha doesn't have any value."

    class NotSaved(Exception):

        def __init__(self):
            super().__init__()
        
        def __str__(self):
            return "Captcha not saved."




class Captcha:
   
    __text = None
    data = None

    def __init__(self, n=5, chars=string.ascii_lowercase, width=250, height=90):
        self.__n = n
        self.__chars = chars
        self.__img = ImageCaptcha(width=width, height=height)
        self.__w = width
        self.__h = height
        self.__id = sha256(os.urandom(32)).hexdigest()

    
    
    @property
    def width(self):
        return self.__w

    @property
    def height(self):
        return self.__h

    @property
    def text_size(self):
        return self.__n

    @property
    def id(self):
        return self.__id


    def genText(self):
        txt = ''
        for i in range(self.__n):
            txt += secrets.choice(self.__chars)

        self.data = base64.b64encode(self.__img.generate(txt).getvalue()).decode()
        self.__text = txt



    def checkValue(self, usr_text: str) -> bool:
        return self.__text == usr_text



def captchaControl(form):
    captcha_id = form.get('captcha-id')
    captcha_answer = form.get('captcha-answer')

    capt = captchas_activated.get(captcha_id)
    if not capt:
        raise CaptchaException
    if not capt.checkValue(captcha_answer):
        del captchas_activated[captcha_id]
        raise CaptchaException

    del captchas_activated[captcha_id]

