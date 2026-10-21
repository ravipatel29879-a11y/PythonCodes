# 3.11 Default Parameter Function

def show_details(person, location="Vadodara", course="MCA"):
    print(f"Name: {person:<10} | City: {location:<10} | Course: {course}")

print("(a) Calling with all 3 arguments:")
show_details("Rahul", "Rajkot", "BCA")

print("\n(b) Calling with only 'person':")
show_details("Neha")

print("\n(c) Calling with 'person' and 'location':")
show_details("Amit", "Bhavnagar")
