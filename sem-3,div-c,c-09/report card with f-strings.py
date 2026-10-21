# 3.10 Report Card with f-strings

student = "Riya Sharma"
registration_no = 20261524
scores = [82, 89, 76, 91, 87]

total_score = sum(scores)
percentage_score = total_score / len(scores)

if percentage_score >= 90:
    grade_result = "A+"
elif percentage_score >= 80:
    grade_result = "A"
elif percentage_score >= 70:
    grade_result = "B"
else:
    grade_result = "C"

print("=" * 40)
print(f"{'STUDENT REPORT CARD':^40}")
print("=" * 40)
print(f"Name   : {student:<25}")
print(f"Roll No: {registration_no:<25}")
print("-" * 40)

# Loop with auto-incrementing index numbers
for subject_no, score in enumerate(scores, start=1):
    print(f"Subject {subject_no} Marks : {score:>5}")

print("-" * 40)
print(f"Total Marks     : {total_score:>5} / 500")
print(f"Percentage      : {percentage_score:>5.2f}%")
print(f"Grade Obtained  : {grade_result:>5}")
print("=" * 40)
