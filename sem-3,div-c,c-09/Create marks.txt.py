# Create result.txt
student_data = [
    "Karan 80\n",
    "Priya 95\n",
    "Aarav 75\n",
    "Meera 90\n",
    "Rohan 65\n",
    "Sneha 85\n"
]

with open("result.txt", "w") as file:
    file.writelines(student_data)

# Read, parse, and calculate class average
marks_total = 0
student_count = 0

with open("result.txt", "r") as file:
    for record in file:
        details = record.strip().split()
        if len(details) == 2:
            student_name, score = details[0], float(details[1])
            marks_total += score
            student_count += 1

average = marks_total / student_count if student_count > 0 else 0
report = f"Total Students: {student_count}\nAverage Marks: {average:.2f}\n"

# Write results to report.txt
with open("report.txt", "w") as file:
    file.write(report)

print("Student Result Summary:")
print(report)