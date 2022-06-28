from hashlib import sha256

class User:

    def __init__(self, id: int, email: str, senha: str, 
            dateCadastro: int, dateBirth: int, funcao: str):

        self.id = id
        self.email = email
        self.senha = senha
        self.dateCadastro = dataCadastro
        self.dateBirth = dateBirth
        self.funcao = funcao

    @property
    def hashPasswd(self) -> str:
        return sha256(self.senha.encode('utf-8')).hexdigest()



