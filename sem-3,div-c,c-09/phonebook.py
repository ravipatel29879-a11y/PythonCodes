contacts = {}

# (a) Add 5 contacts
contacts["Rahul"] = "9123456780"
contacts["Neha"] = "8234567891"
contacts["Amit"] = "7345678902"
contacts["Priya"] = "6456789013"
contacts["Karan"] = "5567890124"

# (b) Search by name
search_person = "Amit"
print(f"Search '{search_person}': {contacts.get(search_person, 'Not Found')}")

# (c) Update a number
contacts["Rahul"] = "9988776655"
print(f"Updated Rahul's number: {contacts['Rahul']}")

# (d) Delete a contact
removed = contacts.pop("Priya", None)
print(f"Deleted contact 'Priya': {removed}")

# (e) Display all contacts sorted by name
print("\nContacts sorted by name:")
for person in sorted(contacts.keys()):
    print(f"  {person:<10} : {contacts[person]}")
