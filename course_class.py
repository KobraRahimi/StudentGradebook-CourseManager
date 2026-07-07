class Course:
    def __init__(self, course_code, course_name, students, assessments):
        self.course_code =course_code
        self.course_name = course_name
        self.students = students
        self.assessments = assessments

    def add_student(self, student_id):
        list_students = [self.students, student_id]
        self.students = list_students

    def add_assessment(self, assessment):
        self.assessments = [self.assessments, assessment]

    def find_assessment(self, title):
        if title in self.assessments:
            print(f"The {title} was found.")
        else:
            print(f"{title} not found.")

    def display_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Enrolled Students: {len(self.students)}")
        print("Assessments: ")
        # print(f"- Quiz 1 / Max Score: 10 \n- Midterm Exam / Max Score: 100 \n- Final Project / Max Score: 100")


