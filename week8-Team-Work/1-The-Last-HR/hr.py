import sqlite3
import requests

conn = sqlite3.connect("hr.db")
cursor = conn.cursor()

""" course_name -> id"""
course_name_to_id = {} 


def create_student(conn, cursor, student):
    insert_query = """
        INSERT INTO Students(name, github)
        VALUES(?, ?)
    """
    
    cursor.execute(insert_query, (student["name"], student["github"]))
    conn.commit()

    return cursor.lastrowid



def create_course(conn, cursor, course):
    insert_query = """
        INSERT INTO Courses(name)
        VALUES(?)
    """

    cursor.execute(insert_query, (course["name"], ))
    conn.commit()

    return cursor.lastrowid



def create_relation(conn, cursor, student_id, course_id):
    insert_query = """
        INSERT INTO Students_to_Courses(student_id, course_id)
        VALUES(?, ?)
    """

    cursor.execute(insert_query, (student_id, course_id))
    conn.commit()


API_URL = "https://hackbulgaria.com/api/students/"
students_data = requests.get(API_URL).json()
all_students = len(students_data)
counter = 0

for student in students_data:
    student_id = create_student(conn, cursor, student)
    courses = student["courses"]
    
    print("Inserting {}".format(student["name"]))

    for course in courses:
        print("Inserting courses for {}".format(student["name"]))
        course_name = course["name"]
        print("Current course: {}".format(course_name))
        if course_name in course_name_to_id:
            course_id = course_name_to_id[course_name]
        else:
            course_id = create_course(conn, cursor, course)
            course_name_to_id[course_name] = course_id


        create_relation(conn, cursor, student_id, course_id)
    
    print("Inserted {}".format(student["name"]))
    print("So far: {}/{}".format(counter, all_students))
    counter += 1

