class Human:
    def __init__(self, person_name, person_age):
        self.person_name = person_name
        self.person_age = person_age

    def display(self):
        print(f"Name   : {self.person_name}")
        print(f"Age    : {self.person_age}")


class Staff(Human):
    def __init__(self, person_name, person_age, income):
        super().__init__(person_name, person_age)
        self.income = income

    def display(self):
        super().display()
        print(f"Salary : ${self.income:,.2f}")


# Personalised details
worker = Staff("Rahul Patel", 24, 75000)
worker.display()