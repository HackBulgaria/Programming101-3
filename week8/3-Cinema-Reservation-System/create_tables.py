import sqlite3
import sys

db_name = sys.argv[1]
sql_file = sys.argv[2]

conn = sqlite3.connect(db_name)

with open(sql_file, "r") as f:
    conn.executescript(f.read())
    conn.commit()

