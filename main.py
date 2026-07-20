from gradebook_class import Gradebook
from project_class import Project
from exam_class import Exam
from quiz_class import Quiz
from student_class import Student
from course_class import Course

student1 = Student("S001", "Ahmad Rahimi", "ahmad@gmail.com")
course1 = Course("PY101", "Python Programming")
quiz1 = Quiz("Quiz1", 10)
exam1 = Exam("Exam1", 100)
project1 = Project("Project1", 100)
gradebook = Gradebook()
gradebook.add_student(student1)
gradebook.add_course(course1)

should_continue = True
while should_continue:
    print("===== Student Gradebook Manager ===== ")
    print("1. Add Student \n2. View Students \n3. Add Course \n4. View Courses \n5. Enroll Student in Course")
    print("6. Add Assignment \n7. Record Grade \n8. View Student Report \n0. Exit ")
    choice = int(input("Choose an option: "))


    if choice == 0:
        should_continue = False

    elif choice == 1:
        print("== Add Student ==")
        stu_id = input("Student ID: ").upper()
        name = input("Name: ").title()
        email = input("Email: ").lower()
        student = Student(stu_id, name, email)
        gradebook.add_student(student)

    elif choice == 2:
        print("== View Students ==")
        print(student1.student_list)

    elif choice == 3:
        print("== Add Course ==")
        course_code = input("Course Code: ").upper()
        course_name = input("Course Name: ").title()
        course = Course(course_code, course_name)
        gradebook.add_course(course)

    elif choice == 4:
        print("View Courses")
        print(course1.course_list)

    elif choice == 5:
        print("== Enroll Student in Course ==")
        student_id = input("Student ID: ").upper()
        course_code = input("Course Code: ").upper()
        gradebook.enroll_student(student_id, course_code)

    elif choice == 6:
        print("== Add Assignment ==")
        course_code = input("enter course code: ")
        assessment = input("enter type assessment: ")
        gradebook.add_assessment(course_code, assessment)

    elif choice == 7:
        print("== Record Grade ==")
        pass

    elif choice == 8:
        print("== View Student Report ==")
        student_id = input("enter student id: ")
        gradebook.show_report(student_id)

    else:
        print("Invalid number!!")

    if choice != 0:
        print("\n" * 5)

