class Human:
    def __init__(self, person_name, person_age):
        self.person_name = person_name
        self.person_age = person_age

    def display(self):
        print(f"Name: {self.person_name}, Age: {self.person_age}")


class Learner(Human):
    def __init__(self, person_name, person_age, roll_no, score):
        super().__init__(person_name, person_age)
        self.roll_no = roll_no
        self.score = score

    def get_grade(self):
        return 'A' if self.score >= 85 else 'B'

    def display(self):
        super().display()  # Reuses parent display method
        print(
            f"Roll: {self.roll_no}, Marks: {self.score}, Grade: {self.get_grade()}"
        )


person1 = Human("General Person", 35)
learner1 = Learner("Rahul Patel", 22, 18, 96)
learner2 = Learner("Neha Joshi", 19, 12, 81)

print("--- Human Details ---")
person1.display()

print("\n--- Learner Details (Using super()) ---")
learner1.display()
print("-")
learner2.display()