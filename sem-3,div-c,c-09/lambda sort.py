learners = [("Rahul", 68), ("Neha", 52), ("Amit", 89), ("Priya", 61), ("Karan", 77)]

# Sort by marks descending using lambda
ranked_learners = sorted(learners, key=lambda learner: learner[1], reverse=True)

print("Students sorted by marks (Descending):")
for student_name, score in ranked_learners:
    print(f"  {student_name:<8}: {score}")

# Filter students with marks >= 60 using lambda
qualified_learners = list(filter(lambda learner: learner[1] >= 60, ranked_learners))

print("\nStudents with marks >= 60:")
for student_name, score in qualified_learners:
    print(f"  {student_name:<8}: {score}")
