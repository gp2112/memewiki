import psycopg2
import os

db_name = os.environ.get('MEMEWIKIDB', 'memewiki')
db_user = os.environ.get('MEMEWIKIDBUSER', 'postgres')

conn = lambda: psycopg2.connect(f"dbname={db_name} user={db_user}")



