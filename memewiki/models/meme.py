from memewiki.models import db
from memewiki.models import user
from memewiki.models import midia
from datetime import datetime



class MemeComment:

    def __init__(self, meme_id: int, datahora: datetime, 
            usuario: user.User, texto: str, midia: midia.Midia):

        self.meme_id = meme_id
        self.datahora = datahora
        self.usuario = usuario
        self.texto = texto
        self.midia = midia

    def commit():
        with db.conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO comentariomeme VALUES (%s,%s,%s,%s,%s);
                """, (self.meme_id, self.datahora, self.usuario.id, 
                        self.texto, self.midia.id))
            conn.commit()




class Meme:

    def __init__(self, id: int, usuario: user.User, datahora: datetime, 
            midia_: midia.Midia):

        self.id = id
        self.usuario = usuario
        self.datahora = datahora
        self.midia = midia_

    def commit(self):

        with db.conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO meme (idusuario, datahora, idmidia)
                    VALUES (%s,%s,%s) RETURNING id;
               """, (self.usuario.id, self.datahora, self.midia.id))
                self.id = cur.fetchone()[0]
            conn.commit()

    def getComments(self) -> list:
        with db.conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                   SELECT * FROM comentariomeme
                        INNER JOIN usuario ON idusuariopublicou=usuario.id
                        LEFT JOIN midia ON idmidia=midia.id
                    WHERE idmeme=%s;
                """, (self.id,))
                r = cur.fetchall()

        comments = []
        for c in r:
            user_ = user.User(*c[5:12])
            midia_ = midia.Midia(*c[12:])

            comments.append(
                MemeComment(c[0], c[1], user_, c[3], midia_)
            )
        return comments

def getMeme(id: int) -> Meme:
    with db.conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM meme
                    LEFT JOIN midia ON idmidia=midia.id
                    INNER JOIN usuario ON idusuario=usuario.id
                    WHERE meme.id=%s;
            """, (id,))
            r = cur.fetchone()

    if len(r) == 0 or r is None:
        raise Exception('Não existe Meme')

    midia_ = midia.Midia(*r[4:7])
    user_ = user.User(*r[7:])

    return Meme(id, user_, r[2], midia_)


def getMemes(limit: int) -> list:
    with db.conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM meme
                    LEFT JOIN midia ON idmidia=midia.id
                    INNER JOIN usuario ON idusuario=usuario.id
                ORDER BY meme.id DESC LIMIT %s;
            """, (limit,))
            r = cur.fetchall()
    memes = []
    for c in r:
        midia_ = midia.Midia(*c[4:7])
        user_ = user.User(*c[7:14])
        memes.append(
            Meme(c[0], user_, c[2], midia_)
        )
    return memes


