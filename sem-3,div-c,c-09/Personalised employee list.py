STUDENT_ID = 32

class Learner:
    def __init__(self, student_name):
        self.student_name = student_name
        self.__score = 0  # Private attribute

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if 0 <= new_score <= 100:
            self.__score = new_score
            print(f"Successfully set score to: {new_score}")
        else:
            raise ValueError(
                f"InvalidScoreError: Score must be between 0 and 100. Got: {new_score}"
            )

learner = Learner("Rahul")
valid_score = STUDENT_ID % 25 + 55  # Personalisation

print("1. Setting valid score...")
learner.set_score(valid_score)
print(f"Getter output: {learner.get_score()}")

print("\n2. Direct private access test...")
try:
    print(learner.__score)
except AttributeError as error:
    print(f"Direct access failed: {error}")

print("\n3. Setting invalid score...")
try:
    learner.set_score(120)
except ValueError as value_error:
    print(f"Caught Error: {value_error}")