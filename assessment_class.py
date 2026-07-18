class Assessment:
    def __init__(self, title, max_score:int):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        """Returns the student's score percentage"""
        if self.max_score == 10:
            return score * 10
        return None

    def grade_message(self, score):
        """Prints a short message based on the student’s score"""
        if 90 <= score <= 100:
            print(f"Excellent 😍")
        elif score >= 80:
            print(f"Good 🤗")
        elif score >= 60:
            print(f"Satisfactory 🙂")
        else:
            print(f"Needs Improvement 😡")

    def display_info(self):
        """Prints the assessment title and maximum score"""
        print(f"{self.title} - Max Score: {self.max_score}")
