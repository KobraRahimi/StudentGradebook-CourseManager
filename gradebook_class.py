from student_class import Student
from course_class import Course

class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = 55

    def add_student(self):
        """Adds a new Student object to the students dictionary in the gradebook, using the student's ID as the key"""
        student_id = input("Student ID: ")
        name = input("Name: ")
        email = input("Email: ")
        self.students[student_id] = Student(student_id, name, email)


    def add_course(self):
        """Adds a new Course object to the courses dictionary using its course_code"""
        course_code = input("Course Code: ")
        course_name = input("Course Name: ")
        self.courses[course_code] = Course(course_code, course_name)


    def enroll_student(self):
        """Connects a student to a course after verifying that both the student and course exist"""
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        if student_id in self.students and course_code in self.courses:

            self.students[student_id].enroll_cource(course_code)
            self.courses[course_code].add_student(course_code)

            print(f"Now student {student_id} is connected to course {course_code}.")


    def add_assessment(self, course_code, assessment):
        """Adds an assessment, such as a quiz, exam, or project, to a specific course"""

    def record_grade(self, student_id, course_code, assessment_title, score):
        """Records a student's score for an assessment in a course after verifying that the student, course, and assessment exist."""

    def calculate_average(self, student_id, course_code):
        """Calculates a student's average grade in a course"""

    def show_report(self, student_id):
        """Shows a student's full report, including name, enrolled courses, grades, average, letter grade, and pass/fail result"""

    def search_student(self, keyword):
        """Searches for students by ID or name"""

    def delete_student(self, student_id):
        """Removes a student from the gradebook and their enrolled courses"""

    def get_result(self, average):
        """Returns whether a student passed or failed based on the passing grade"""


