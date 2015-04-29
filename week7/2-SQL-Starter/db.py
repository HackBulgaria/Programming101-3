import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

create_users_table = """
CREATE TABLE IF NOT EXISTS 
users(id INTEGER PRIMARY KEY, email TEXT, gender TEXT)
"""

cursor.execute(create_users_table)
connection.commit()
