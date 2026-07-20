from gradebook_class import Gradebook

gradebook = Gradebook()

should_continue = True
while should_continue:
    print("===== Student Gradebook Manager ===== ")
    print("1. Add Student \n2. View Students \n3. Add Course \n4. Enroll Student in Course")
    print("5. Add Assignment \n6. Record Grade \n7. View Student Report \n0. Exit ")
    choice = int(input("Choose an option: "))


    if choice == 0:
        should_continue = False

    elif choice == 1:
        gradebook.add_student()

    elif choice == 2:
        print(gradebook.students)

    elif choice == 3:
        gradebook.add_course()

    elif choice == 4:
        gradebook.enroll_student()

    elif choice == 5:
        course_code = input("enter course code: ")
        assessment = input("enter type assessment: ")
        gradebook.add_assessment(course_code, assessment)

    elif choice == 6:
        pass

    elif choice == 7:
        student_id = input("enter student id: ")
        gradebook.show_report(student_id)

    else:
        print("Invalid number!!")

    if choice != 0:
        print("\n" * 17)

