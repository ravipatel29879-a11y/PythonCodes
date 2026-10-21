import json

class PhoneDirectory:
    def __init__(self, file_name="phonebook.json"):
        self.file_name = file_name
        self.phone_records = {}

    def add_contact(self, person_name, mobile_number):
        self.phone_records[person_name] = mobile_number

    def search(self, person_name):
        print(f"Searching '{person_name}': {self.phone_records.get(person_name, 'Not Found')}")

    def delete(self, person_name):
        if person_name in self.phone_records:
            del self.phone_records[person_name]
            print(f"Removed: {person_name}")

    def display_all(self):
        print("\n--- Phone Directory ---")
        for contact, number in self.phone_records.items():
            print(f"{contact:<20}: {number}")

    def save_to_file(self):
        with open(self.file_name, "w") as file:
            json.dump(self.phone_records, file, indent=4)

    def load_from_file(self):
        try:
            with open(self.file_name, "r") as file:
                self.phone_records = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.file_name}' not found. Creating an empty directory.")

directory = PhoneDirectory()
directory.load_from_file()

# Personalisation: Own contact as first entry
directory.add_contact("Rahul Patel (Self)", "9123456780")
directory.add_contact("Amit Shah", "9234567891")
directory.add_contact("Neha Joshi", "9345678902")
directory.add_contact("Karan Mehta", "9456789013")
directory.add_contact("Priya Desai", "9567890124")

directory.display_all()
directory.search("Rahul Patel (Self)")
directory.delete("Karan Mehta")
directory.save_to_file()