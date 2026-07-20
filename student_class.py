class Student:
    student_list = []
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.__email = email
        self.courses = []
        Student.student_list.append(self.name)

    def get_id(self):
        """Returns the student's ID"""
        return self.student_id

    def get_name(self):
        """Returns the student's name"""
        return self.name

    @property
    def email(self):
        """Returns the student's email address"""
        return self.__email

    @email.setter
    def email(self, set_email):
        """Updates the student’s email address. It can check that the email is valid before changing it"""
        if set_email.endswith("@gmail.com"):
            self.__email = set_email
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
        print(f"Email: {self.__email}")
        print(f"Courses: {self.courses}")
