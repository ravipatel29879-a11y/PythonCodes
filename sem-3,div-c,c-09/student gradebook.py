student_marks = {
    "Rahul": [78, 85, 91],
    "Neha": [72, 68, 84],
    "Amit": [89, 93, 87],
    "Priya": [81, 86, 90]
}

# Calculate averages
average_marks = {name: sum(scores) / len(scores) for name, scores in student_marks.items()}

# Sort by average (highest first)
ranked_students = sorted(average_marks.items(), key=lambda item: item[1], reverse=True)

print(f"{'Student Name':<15} | {'Average Mark':<12}")
print("-" * 32)
for name, average in ranked_students:
    print(f"{name:<15} | {average:<12.2f}")

best_student = ranked_students[0]
print("-" * 32)
print(f"Top Student: {best_student[0]} with Average: {best_student[1]:.2f}")
