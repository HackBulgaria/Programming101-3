import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

create_users_table = """
CREATE TABLE IF NOT EXISTS 
users(id INTEGER PRIMARY KEY, email TEXT, gender TEXT)
"""

insert_users = """
INSERT INTO users(email, gender)
VALUES ("asd@asd.com", "male"),
       ("asd2@asd.com", "female") 
"""


cursor.execute(create_users_table)
cursor.execute(insert_users)
connection.commit()
