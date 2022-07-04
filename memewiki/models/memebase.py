from memewiki.models import db
from memewiki.models import midia
from memewiki.models import user
from memewiki.models import meme
from datetime import datetime



class MemeBase:

    def __init__(self, id: int, titulo: str, thumb: midia.Midia, 
            datahorapub: datetime, datahoraedicao: datetime,
            usuarioedicao: user.User, text: str, usuariopub: user.User):
        self.id = id
        self.titulo = titulo
        self.thumb = thumb
        self.datahorapub = datahorapub
        self.datahoraedicao = datahoraedicao
        self.usuarioedicao = usuarioedicao
        self.text = text
        self.usuariopub = usuariopub

    def getMemes(self):
        with db.conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT idmemebase, meme.id, meme.datahora, 
                        meme.mediaavaliacoes, meme.numeroavaliacoes, midia.id, 
                        midia.formato, midia.url, usuario.id, usuario.email, 
                        usuario.senha, usuario.nome, usuario.datahoracadastro, 
                        usuario.datanascimento, usuario.funcao
                    FROM compoememebase
                    
                    INNER JOIN meme ON idmeme=meme.id
                    INNER JOIN midia ON meme.idmidia=midia.id
                    INNER JOIN usuario ON meme.idusuario=usuario.id
                    
                    WHERE idmemebase=%s;

                """, (self.id, ))
                r = cur.fetchall()

        memes = []
        for c in r:
            midia_ = midia.Midia(*c[5:8])
            user_ = user.User(*c[8:])
            meme_ = meme.Meme(c[0], user_, *c[1:5])
            memes.append(meme_)

        return memes

    def commit(self):
        with db.conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO memebase (titulo, thumb, datahorapublicacao, 
                        richtext, idusuariopublicou) VALUES
                    (%s,%s,%s,%s,%s) RETURNING id;
                """, (self.titulo, self.thumb.id, self.datahorapub,
                    self.text, self.usuariopub.id))

                self.id = cur.fetchone()[0]
            conn.commit()

def memebaseByName(name: str):
    with db.conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM memebase
                INNER JOIN midia
                    ON thumb=midia.id
                INNER JOIN usuario AS usuariopub
                    ON idusuariopublicou=usuariopub.id
                LEFT JOIN usuario AS usuarioedit
                    ON usuarioedicao=usuarioedit.id
                WHERE titulo=%s;
            """, (name,))
            r = cur.fetchone()

    if not r:
        return None
    midia_ = midia.Midia(*r[8:11])
    user_pub = user.User(*r[11:18])
    user_edit = user.User(*r[18:])


    return MemeBase(*r[:2], midia_, *r[3:5], user_edit, r[6], user_pub)

def getLastMemes(limit: int) -> list:
    with db.conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM memebase
                INNER JOIN midia
                    ON thumb=midia.id
                INNER JOIN usuario AS usuariopub
                    ON idusuariopublicou=usuariopub.id
                LEFT JOIN usuario AS usuarioedit
                    ON usuarioedicao=usuarioedit.id
                ORDER BY memebase.id DESC LIMIT %s;
            """, (limit, ))

            r = cur.fetchall()
    memesbase = []
    for c in r:
        midia_ = midia.Midia(*c[8:11])
        user_pub = user.User(*c[11:18])
        user_edit = user.User(*c[18:])

        memesbase.append(
            MemeBase(*c[:2], midia_, *c[3:5], user_edit, c[6], user_pub)
        )
    return memesbase

