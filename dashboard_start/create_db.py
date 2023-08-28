import sqlite3, os

DBFILE = "aqi.db"
SQLFILE = "create_aqi_table.sql"

cur_dir = os.path.dirname(os.path.abspath(__file__))
sql_path = os.path.join(cur_dir, SQLFILE)


if os.path.exists(DBFILE):
    os.remove(DBFILE)

conn = sqlite3.connect(DBFILE)
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS aqi")

with open(sql_path) as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()
