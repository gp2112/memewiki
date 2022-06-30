from memewiki.models import db

class User:

    def __init__(self, id: int, email: str, senha: str, nome: str,
            dateCadastro: int, dateBirth: int, funcao: str):

        self.id = id
        self.email = email
        self.nome = nome
        self.senha = senha        
        self.dateCadastro = dateCadastro
        self.dateBirth = dateBirth
        self.funcao = funcao

    def commit(self):
        with db.conn() as conn:
            with conn.cursor() as cur:
                print(self.__dict__.values())
                if not self.id:
                    cur.execute("""
                        INSERT INTO usuario
                        (email, senha, nome, datahoracadastro, datanascimento, funcao)
                        VALUES (%s, %s, %s, %s, %s, %s);
                    """, (self.email, self.senha, self.nome, 
                                        self.dateCadastro, self.dateBirth, self.funcao))

                else:
                    cur.execute("""
                        UPDATE usuario
                        SET email=%s, nome=%s, senha=%s, datahoracadastro=%s, 
                        datanascimento=%s, funcao=%s WHERE id=%s;
                    """, (self.email, self.senha, self.nome, 
                                    self.dateCadastro, self.dateBirth, 
                                    self.funcao, self.id))
            conn.commit()

def getUserByName(nome: str) -> User:
    with db.conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM usuario WHERE nome=%s;        
            """, (nome,))
            user = cur.fetchone()
    if not user:
        return None
    return User(*user)

def getUserByEmail(email: str) -> User:
    with db.conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM usuario WHERE email=%s;        
            """, (email,))
            user = cur.fetchone()
    if not user:
        return None
    return User(*user)




