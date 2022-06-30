from memewiki.models import db




class ThreadComment:

    def __init__(self, idusuario: int, idthread: int, 
                    datahora: int, texto: str, idmidia: int):
        
        self.idusuario = idusuario
        self.datahora = datahora
        self.idthread = idthread
        self.texto = texto
        self.idmidia = idmidia

    def commit(self):
        with db.conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO threadcomentario (idusuario, datahora, idthread, texto, idmidia)
                    VALUES (%s,%s,%s,%s,%s)
                """, self.idusuario, self.datahora, self.idthread, self.texto, self.idmidia)
            conn.commit()


class Thread:

    def __init__(self, idUsuario: int, datahora: int, titulo: str,
            desc: str, idmidia: int, id: int = None):
        self.idusuario = idUsuario
        self.datahora = datahora
        self.titulo = titulo
        self.desc = descricao
        self.idmidia = idmidia

    def getComments(self, limit=100):
        comments = [] 
        with db.conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT * FROM threadcomentario 
                    LEFT JOIN midia ON
                    threadcomentario.idmidia=midia.id
                    WHERE idthread=%s LIMIT %s;
                """, (self.id, limit))
                comments = cur.fetchall()
        
        return [ ThreadComment(*c) for c in comments ]

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
                    INSERT INTO thread (idusuario, datahora, titulo, desc, idmidia)
                    VALUES (%s,%s,%s,%s,%s)
                """, self.idusuario, self.datahora, self.titulo, self.desc, self.idmidia)
            conn.commit()

def get_thread(id: int) -> Thread:
    with db.conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM thread
                LEFT JOIN midia ON
                thread.idmidia=midia.id
                WHERE thread.id=%s;
            """, (id,))
            thread = cur.fetchone()
        
    return Thread(thread[1:-3], thread[-1], id=thread[0])

def get_last_threads(n: int, last_id: int=None) -> list:
    with db.conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM thread 
                LEFT JOIN midia ON
                thread.idmidia=midia.id
                ORDER BY datahora DESC LIMIT %s;
            """, (n,))
            threads = cur.fetchall()

    return [ Thread(thread[1:-3], thread[-1], id=thread[0]) for thread in threads]






