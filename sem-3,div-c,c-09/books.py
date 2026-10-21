class LibraryBook:
    def __init__(self, book_name):
        self.book_name = book_name
        self.__is_available = True

    def issue(self):
        if self.__is_available:
            self.__is_available = False
            print(f"SUCCESS: '{self.book_name}' issued.")
        else:
            print(f"FAILED: '{self.book_name}' already issued.")

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            print(f"SUCCESS: '{self.book_name}' returned.")
        else:
            print(f"NOTICE: '{self.book_name}' was already available.")

# 2 Favourite books
book1 = LibraryBook("Python Basics")
book2 = LibraryBook("Data Structures")

print("--- Complete Issue-Return Cycle ---")
book1.issue()
book1.issue()
book1.return_book()
book1.return_book()

print("\n--- Second Book Cycle ---")
book2.issue()
book2.return_book()