class Learner:
    def __init__(self, student_name, roll_no, score):
        self.student_name = student_name
        self.roll_no = roll_no
        self.score = score

    def display(self):
        print(f"Roll: {self.roll_no:<3} | Name: {self.student_name:<20} | Marks: {self.score}")


class LearnerManager:
    def __init__(self):
        self.learner_list = []

    def add_student(self, learner):
        self.learner_list.append(learner)

    def display_all(self):
        print("\n--- All Learners ---")
        for item in self.learner_list:
            item.display()

    def search_by_name(self, search_name):
        print(f"\n--- Search Result for '{search_name}' ---")
        matched = [
            item for item in self.learner_list
            if search_name.lower() in item.student_name.lower()
        ]
        for item in matched:
            item.display()

    def find_top_scorer(self):
        topper = max(self.learner_list, key=lambda item: item.score)
        print("\n--- Highest Scorer ---")
        topper.display()


manager = LearnerManager()
manager.add_student(Learner("Rahul Patel", 12, 89))
manager.add_student(Learner("Neha Joshi", 18, 84))
manager.add_student(Learner("Amit Shah", 21, 93))
manager.add_student(Learner("Pooja Desai", 27, 79))
manager.add_student(Learner("Karan Mehta", 32, 86))

manager.display_all()
manager.search_by_name("Rahul")
manager.find_top_scorer()