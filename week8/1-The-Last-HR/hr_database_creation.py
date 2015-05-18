import sqlite3


CREATE_STUDENTS = """
CREATE TABLE IF NOT EXISTS Students(
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    github TEXT
)
"""

CREATE_COURSES = """
CREATE TABLE IF NOT EXISTS Courses(
    course_id INTEGER PRIMARY KEY,
    name TEXT
)
"""

STUDENTS_TO_COURSES = """
CREATE TABLE IF NOT EXISTS Students_to_Courses(
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(student_id),
    FOREIGN KEY(course_id) REFERENCES Courses(course_id)
)
"""

conn = sqlite3.connect("hr.db")
cursor = conn.cursor()

for table in [CREATE_STUDENTS, CREATE_COURSES, STUDENTS_TO_COURSES]:
    cursor.execute(table)

