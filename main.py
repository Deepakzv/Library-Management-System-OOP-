import pickle

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open("library.dat", "rb") as file:
                self.books = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.books = []

    def save_books(self):
        with open("library.dat", "wb") as file:
            pickle.dump(self.books, file)

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        self.books.append(Book(title, author))
        self.save_books()
        print("Book added.")

    def view_books(self):
        for book in self.books:
            status = "Issued" if book.issued else "Available"
            print(f"{book.title} by {book.author} - {status}")

    def issue_book(self):
        title = input("Enter book title to issue: ")
        for book in self.books:
            if book.title.lower() == title.lower() and not book.issued:
                book.issued = True
                self.save_books()
                print("Book issued.")
                return
        print("Book not available or already issued.")

    def return_book(self):
        title = input("Enter book title to return: ")
        for book in self.books:
            if book.title.lower() == title.lower() and book.issued:
                book.issued = False
                self.save_books()
                print("Book returned.")
                return
        print("Book not found or not issued.")

library = Library()

while True:
    print("\n--- Library Management ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        library.add_book()
    elif choice == '2':
        library.view_books()
    elif choice == '3':
        library.issue_book()
    elif choice == '4':
        library.return_book()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
