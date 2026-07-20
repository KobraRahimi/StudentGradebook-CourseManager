class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = 55

    def add_student(self, student):
        """Adds a new Student object to the students dictionary in the gradebook, using the student's ID as the key"""
        self.students[student.get_id()] = student


    def add_course(self,course):
        """Adds a new Course object to the courses dictionary using its course_code"""
        self.courses[course.course_code] = course


    def enroll_student(self, student_id, course_code):
        """Connects a student to a course after verifying that both the student and course exist"""

        if student_id.upper() in self.students:
            if course_code.upper() in self.courses:
                self.students[student_id].enroll_course(course_code)
                self.courses[course_code].add_student(student_id)
                print(f"Now student {student_id} is connected to course {course_code}.")
            else:
                print("The course ID is not in the courses dictionary!")
        else:
            print("The student ID is not in the students dictionary!")


    def add_assessment(self, course_code, assessment):
        """Adds an assessment, such as a quiz, exam, or project, to a specific course"""

    def record_grade(self, student_id, course_code, assessment_title, score):
        """Records a student's score for an assessment in a course after verifying that the student, course, and assessment exist."""
        if student_id in self.students and course_code in self.courses:
            if self.courses[course_code].find_assessment(assessment_title):
                pass


    def calculate_average(self, student_id, course_code):
        """Calculates a student's average grade in a course"""

    def show_report(self, student_id):
        """Shows a student's full report, including name, enrolled courses, grades, average, letter grade, and pass/fail result"""
        print("===== Student Report =====")
        self.students[student_id].display_info()

    def search_student(self, keyword):
        """Searches for students by ID or name"""

    def delete_student(self, student_id):
        """Removes a student from the gradebook and their enrolled courses"""
        del self.students[student_id]

    def get_result(self, average):
        """Returns whether a student passed or failed based on the passing grade"""
        if average >= self.passing_grade:
            print("Passed")
        else:
            print("Failed")
