import sqlite3

db = sqlite3.connect("users.db")
cursor = db.cursor()

select_one = """
SELECT id, email, gender
FROM users
WHERE id = 1
"""

cursor_result = cursor.execute(select_one)
row = cursor_result.fetchone()

print(row)

