from memewiki.models import db

class Midia:

    def __init__(self, id: int, formato: str, url: str):
        self.id = id
        self.formato = formato
        self.url = url

    def commit(self):
        with db.conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO midia (formato, url)
                    VALUES (%s,%s) RETURNING id;
                """, (self.formato, self.url))
                self.id = cur.fetchone()[0]
            conn.commit()


def getMidia(id: int) -> Midia:
    with db.conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM midia 
                WHERE id=%s;
            """, (id,))
            r = cur.fetchone()
    return Midia(id, r[1], r[2])




