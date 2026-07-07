class Student:
    def __init__(self, student_id, name, email, courses):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = courses

    def get_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def set_email(self, email):
        if email.endswith("@gmail.com"):
            self.email = email
        else:
            print("Invalid email")

    def enroll_course(self, course_code):
        list_courses = [self.courses, course_code]
        self.courses = list_courses

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Courses: {self.courses}")

