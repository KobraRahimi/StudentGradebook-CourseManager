class Course:
    course_list = []
    def __init__(self, course_code, course_name):
        self.course_code =course_code
        self.course_name = course_name
        self.students = []
        self.assessments = []
        Course.course_list.append(course_name)

    def add_student(self, student_id):
        """Enrolls a student in this course by adding the student’s ID to the course’s students list"""
        if not student_id.upper() in self.students:
            self.students.append(student_id)
        else:
            print("The student ID is on the list!")

    def add_assessment(self, assessment):
        """Adds a quiz, exam, or project to the course"""
        self.assessments.append(assessment)

    def find_assessment(self, title):
        """Searches for an assessment by title"""
        return title.lower() or title.title() in self.assessments

    def display_info(self):
        """Shows course details, such as course code, course name, number of students, and assessments"""
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Enrolled Students: {len(self.students)}")
        print("Assessments: ")
        # print(f"- Quiz 1 / Max Score: 10 \n- Midterm Exam / Max Score: 100 \n- Final Project / Max Score: 100")