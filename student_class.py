class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []

    def get_id(self):
        """Returns the student's ID"""
        return self.student_id

    def get_name(self):
        """Returns the student's name"""
        return self.name

    def set_email(self, email):
        """Updates the student’s email address. It can check that the email is valid before changing it"""
        if email.endswith("@gmail.com"):
            self.email = email
        else:
            print("Invalid email")

    def enroll_course(self, course_code):
        """Adds a course code to the student’s courses list."""
        if not course_code.upper() in self.courses:
            self.courses.append(course_code)
        else:
            print("The course code is included in the list!")

    def display_info(self):
        """Shows the student’s basic information, such as ID, name, email, and enrolled courses"""
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Courses: {self.courses}")
