import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='password',
    port='5432'
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE my_database")

cursor.close()
conn.close()