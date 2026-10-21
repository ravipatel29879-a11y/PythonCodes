# Personalisation
STUDENT_ID = 32
AUTHOR_NAME = "Rahul Patel"  # Your details

class Learner:
    def __init__(self, student_name, roll_no, scores):
        self.student_name = student_name
        self.roll_no = roll_no
        self.scores = scores  # List of 4 subject marks

    def get_percentage(self):
        return sum(self.scores) / len(self.scores)

    def get_grade(self):
        percentage = self.get_percentage()
        if percentage >= 90:
            return 'A+'
        elif percentage >= 80:
            return 'A'
        elif percentage >= 70:
            return 'B'
        else:
            return 'C'

    def display(self):
        print(
            f"Roll: {self.roll_no:<3} | Name: {self.student_name:<20} | "
            f"Percentage: {self.get_percentage():.2f}% | Grade: {self.get_grade()}"
        )


# 3 Learner objects (One is the programmer)
learner1 = Learner(AUTHOR_NAME, STUDENT_ID, [85, 88, 91, 87])
learner2 = Learner("Amit Shah", 16, [72, 80, 76, 84])
learner3 = Learner("Neha Joshi", 21, [90, 86, 89, 92])

for learner in [learner1, learner2, learner3]:
    learner.display()