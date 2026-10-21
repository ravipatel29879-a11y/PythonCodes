ID_NUMBER = 32

class Learner:
    total_count = 0  # Class attribute

    def __init__(self, student_name):
        self.student_name = student_name
        Learner.total_count += 1

# Personalisation limit: id_number % 4 + 3
creation_limit = ID_NUMBER % 4 + 3

student_names = [
    "Rahul", "Neha", "Amit", "Pooja",
    "Karan", "Meera", "Jay"
]

print(f"Creating objects until limit = {creation_limit}...\n")

for index in range(creation_limit):
    learner = Learner(student_names[index])
    print(f"Created learner {index + 1}: {learner.student_name}")

print(f"\nFinal Learner.total_count: {Learner.total_count}")