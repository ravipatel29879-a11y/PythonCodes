subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))
subject4 = float(input("Enter marks for Subject 4: "))
subject5 = float(input("Enter marks for Subject 5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percent = (total_marks / 500.0) * 100
avg_marks = total_marks / 5.0

print(f"\nTotal Marks: {total_marks:.2f}/500")
print(f"Percentage: {percent:.2f}%")
print(f"Average Marks: {avg_marks:.2f}")
