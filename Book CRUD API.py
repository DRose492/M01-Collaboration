class Book:
    def __init__(self, book_id, book_name, author, publisher):
        self.id = book_id
        self.book_name = book_name
        self.author = author
        self.publisher = publisher

class BookAPI:
    def __init__(self):
        self.books = {}
        self.current_id = 1

    def add_book(self, book_name, author, publisher):
        new_book = Book(self.current_id, book_name, author, publisher)
        self.books[self.current_id] = new_book
        self.current_id += 1
        return new_book

    def get_book(self, book_id):
        return self.books.get(book_id)

    def get_all_books(self):
        return list(self.books.values())

    def update_book(self, book_id, book_name=None, author=None, publisher=None):
        book = self.books.get(book_id)
        if book:
            if book_name:
                book.book_name = book_name
            if author:
                book.author = author
            if publisher:
                book.publisher = publisher
            return book
        return None

    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False

# Usage example:

book_api = BookAPI()

# Add books
book_api.add_book("Book 1", "Author 1", "Publisher 1")
book_api.add_book("Book 2", "Author 2", "Publisher 2")

# Get all books
all_books = book_api.get_all_books()
for book in all_books:
    print(f"Book ID: {book.id}, Name: {book.book_name}, Author: {book.author}, Publisher: {book.publisher}")

# Get a specific book
specific_book = book_api.get_book(1)
if specific_book:
    print(f"Found Book ID: {specific_book.id}, Name: {specific_book.book_name}, Author: {specific_book.author}, Publisher: {specific_book.publisher}")
else:
    print("Book not found")

# Update a book
updated_book = book_api.update_book(1, book_name="Updated Book 1")
if updated_book:
    print(f"Updated Book ID: {updated_book.id}, Name: {updated_book.book_name}, Author: {updated_book.author}, Publisher: {updated_book.publisher}")
else:
    print("Book not found")

# Delete a book
delete_result = book_api.delete_book(2)
if delete_result:
    print("Book deleted")
else:
    print("Book not found")
