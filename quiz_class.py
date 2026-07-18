from assessment_class import Assessment

class Quiz(Assessment):
    def grade_message(self, score):
        """Overrides the parent Assessment method to give feedback for a quiz score"""
        if score >= 9:
            print(f"Great quiz result 😍")
        elif score >= 8:
            print(f"Great job 🤗")
        elif score >= 6:
            print(f"Good effort 🙂")
        else:
            print(f"Needs more practice 😡")

    def display_info(self):
        """Overrides the parent Assessment method so the quiz can display quiz specific information"""
        print(f"Quiz: {self.title} - Max Score: {self.max_score}")