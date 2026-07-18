from assessment_class import Assessment

class Exam(Assessment):
    def grade_message(self, score):
        """Overrides the parent Assessment method to give exam-specific feedback"""
        if 55 <= score <= 100:
            print(f"Passed exam")
        elif 0 <= score < 55:
            print(f"Failed exam")
        else:
            print(f"Invalid score")

    def display_info(self):
        """Overrides the parent method to show that this assessment is an exam"""
        print(f"Exam: {self.title} - Max Score: {self.max_score}")