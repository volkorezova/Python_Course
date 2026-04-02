from db import engine, Session, Base
from models import Student, Course
import random

# DB INIT
def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

# CREATE COURSES
def create_courses(session):
    courses = [
        Course(title="Math"),
        Course(title="Physics"),
        Course(title="Biology"),
        Course(title="History"),
        Course(title="Programming")
    ]
    session.add_all(courses)
    session.commit()
    return courses

# CREATE 20 STUDENTS
def create_students(session, courses):
    for i in range(20):
        student = Student(name=f"Student_{i+1}")
        student.courses = random.sample(courses, k=random.randint(1, 3))
        session.add(student)

    session.commit()

# GET ALL STUDENTS
def print_all_students(session):
    print("\n--- All students ---")
    students = session.query(Student).all()
    for s in students:
        print(s.name)

# ADD NEW STUDENT
def add_student(session, name, course_title):
    student = Student(name=name)
    course = session.query(Course).filter_by(title=course_title).first()
    student.courses.append(course)

    session.add(student)
    session.commit()

    return student

# GET STUDENTS BY COURSE
def print_students_in_course(session, course_title):
    print(f"\nStudents in {course_title}:")
    course = session.query(Course).filter_by(title=course_title).first()
    for s in course.students:
        print(s.name)

# GET COURSES BY STUDENT
def print_courses_of_student(session, student_name):
    print(f"\nCourses of {student_name}:")
    student = session.query(Student).filter_by(name=student_name).first()
    for c in student.courses:
        print(c.title)

# UPDATE STUDENT
def update_student(session, old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if student:
        student.name = new_name
        session.commit()

# DELETE STUDENT
def delete_student(session, name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()

def main():
    init_db()

    session = Session()

    courses = create_courses(session)
    create_students(session, courses)

    print_all_students(session)

    add_student(session, "Tanya", "Math")

    print_students_in_course(session, "Math")
    print_courses_of_student(session, "Tanya")

    update_student(session, "Tanya", "Tanya Updated")
    delete_student(session, "Tanya Updated")

    # to check that student "Tanya Updated" was deleted
    print_all_students(session)

    session.close()


if __name__ == "__main__":
    main()