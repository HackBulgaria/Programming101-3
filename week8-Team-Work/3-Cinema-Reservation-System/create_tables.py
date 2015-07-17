import sqlite3
import sys
from settings import DB_NAME, SQL_FILE


conn = sqlite3.connect(DB_NAME)

with open(SQL_FILE, "r") as f:
    conn.executescript(f.read())
    conn.commit()

