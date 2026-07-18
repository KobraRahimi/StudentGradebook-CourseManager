from assessment_class import Assessment

class Project(Assessment):
    def grade_message(self, score):
        """Overrides the parent Assessment method to give project-specific feedback"""
        if 90 <= score <= 100:
            print(f"Excellent project!")
        elif 55 <= score < 90:
            print(f"Project submitted!")
        elif 0 <= score < 55:
            print(f"Project needs improvement!")
        else:
            print(f"Invalid project score!")

    def display_info(self):
        """Overrides the parent method to show that this assessment is a project"""
        print(f"Project: {self.title} - Max Score: {self.max_score}")