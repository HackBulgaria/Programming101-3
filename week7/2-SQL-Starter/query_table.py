import sqlite3

db = sqlite3.connect("users.db")
db.row_factory = sqlite3.Row

cursor = db.cursor()

select_one = """
SELECT email, id, gender
FROM users
WHERE id = 1
"""

cursor_result = cursor.execute(select_one)

row = cursor_result.fetchone()
print(row["email"])

