from memewiki.models import db
from memewiki.models import midia
from memewiki.models import user

class ThreadComment:

    def __init__(self, usuario: user.User, idthread: int, 
                    datahora: int, texto: str, midia: midia.Midia):
        
        self.usuario = usuario
        self.datahora = datahora
        self.idthread = idthread
        self.texto = texto
        self.midia = midia

    def commit(self):
        with db.conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO threadcomentario (idusuario, datahora, idthread, texto, idmidia)
                    VALUES (%s,%s,%s,%s,%s)
                """, (self.usuario.id, self.datahora, self.idthread, self.texto, self.midia.id if self.midia else None))
            conn.commit()


class Thread:

    def __init__(self, usuario: user.User, datahora: int, titulo: str,
            desc: str, midia: midia.Midia=None, id: int = None):

        self.id = id
        self.usuario = usuario
        self.datahora = datahora
        self.titulo = titulo
        self.desc = desc
        self.midia = midia

    def getComments(self):
        with db.conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT * FROM threadcomentario 
                    LEFT JOIN midia ON
                        threadcomentario.idmidia=midia.id
                    INNER JOIN usuario ON
                        threadcomentario.idusuario=usuario.id
                    WHERE idthread=%s;
                """, (self.id, ))
                r = cur.fetchall()
        comments = []
        for c in r:
            user_ = user.User(*c[8:15])
            midia_ = None
            if c[5]:
                midia_ = midia.Midia(*c[5:8])
            comments.append(
                ThreadComment(user_, *c[1:4], midia_)
            )
        return comments

    def getTags(self):
        with db.conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT tag FROM threadtags 
                    WHERE idthread=%s;
                """, (self.id,))
                tags = cur.fetchall()
        
        return tags

    def commit(self):
        with db.conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO thread (idusuario, datahora, titulo, descricao, idmidia)
                    VALUES (%s,%s,%s,%s,%s) RETURNING id;
                """, (self.usuario.id, self.datahora, self.titulo, self.desc, self.midia.id))
                self.id = cur.fetchone()[0]
            conn.commit()


def get_thread(id: int) -> Thread:
    with db.conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM thread
                LEFT JOIN midia ON
                    thread.idmidia=midia.id
                INNER JOIN usuario ON
                    thread.idusuario=usuario.id
                WHERE thread.id=%s;
            """, (id,))
            r = cur.fetchone()
    midia_ = midia.Midia(*r[6:9])
    user_ = user.User(*r[9:])
    thread = Thread(user_, *r[2:5], midia_, r[0])
        
    return thread
    
def get_last_threads(n: int, last_id: int=None) -> list:
    with db.conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM thread 
                LEFT JOIN midia ON
                    thread.idmidia=midia.id
                INNER JOIN usuario ON
                    thread.idusuario=usuario.id
                ORDER BY thread.id DESC LIMIT %s;
            """, (n,))
            r = cur.fetchall()
    
    threads = []
    for thread in r:
        midia_ = midia.Midia(*thread[6:9])
        user_ = user.User(*thread[9:])
        threads.append( 
                Thread(user_, *thread[2:5], midia_, thread[0])
        )

    return threads






