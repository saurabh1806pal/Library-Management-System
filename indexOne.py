# Library Management System

# A list to store books as dictionaries
books = []
members = []

# Function to display menu options
def show_menu():
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. View Books")
    print("3. Update a Book")
    print("4. Delete a Book")
    print("5. Add a Member")
    print("6. View Members")
    print("7. Borrow a Book")
    print("8. Return a Book")
    print("9. Exit")

# Function to add a new book
def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    status = 'Available'
    books.append({"ID": book_id, "Title": title, "Author": author, "Year": year, "Status": status})
    print("Book added successfully!")

# Function to view all books
def view_books():
    if not books:
        print("No books available.")
    else:
        print("\nList of Books:")
        for book in books:
            print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Year: {book['Year']}, Status: {book['Status']}")

# Function to update book details
def update_book():
    book_id = input("Enter the book ID to update: ")
    for book in books:
        if book['ID'] == book_id:
            book['Title'] = input("Enter new title: ")
            book['Author'] = input("Enter new author: ")
            book['Year'] = input("Enter new publication year: ")
            print("Book updated successfully!")
            return
    print("Book not found.")

# Function to delete a book
def delete_book():
    book_id = input("Enter the book ID to delete: ")
    global books
    books = [book for book in books if book['ID'] != book_id]
    print("Book deleted successfully!")

# Function to add a new member
def add_member():
    member_id = input("Enter member ID: ")
    name = input("Enter member name: ")
    members.append({"ID": member_id, "Name": name, "Borrowed Books": []})
    print("Member added successfully!")

# Function to view all members
def view_members():
    if not members:
        print("No members available.")
    else:
        print("\nList of Members:")
        for member in members:
            print(f"ID: {member['ID']}, Name: {member['Name']}, Borrowed Books: {', '.join(member['Borrowed Books'])}")

# Function for borrowing a book
def borrow_book():
    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")
    for member in members:
        if member['ID'] == member_id:
            for book in books:
                if book['ID'] == book_id and book['Status'] == 'Available':
                    book['Status'] = 'Borrowed'
                    member['Borrowed Books'].append(book['Title'])
                    print("Book borrowed successfully!")
                    return
            print("Book not available.")
            return
    print("Member not found.")

# Function for returning a book
def return_book():
    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")
    for member in members:
        if member['ID'] == member_id:
            for book in books:
                if book['ID'] == book_id and book['Title'] in member['Borrowed Books']:
                    book['Status'] = 'Available'
                    member['Borrowed Books'].remove(book['Title'])
                    print("Book returned successfully!")
                    return
            print("Book not found in member's borrowed list.")
            return
    print("Member not found.")

# Main function
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ")
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            update_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            add_member()
        elif choice == '6':
            view_members()
        elif choice == '7':
            borrow_book()
        elif choice == '8':
            return_book()
        elif choice == '9':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
