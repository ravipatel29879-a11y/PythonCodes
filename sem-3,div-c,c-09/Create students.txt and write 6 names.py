# (a) Create students.txt and write 6 names
students = ["Rahul", "Neha", "Amit", "Pooja", "Karan", "Meera"]

with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

# (b) Read and display all names
print("Student Names:")

with open("students.txt", "r") as file:
    data = file.readlines()
    for item in data:
        print(item.strip())

# (c) Count total lines
print(f"\nTotal students in file: {len(data)}")