class Book:
    """
    Represents a book in the library.

    Attributes:
        book_id (str): Unique identifier for the book.
        title (str): Title of the book.
        author (str): Author of the book.
        isbn (str): ISBN number of the book.
        total_copies (int): Total number of copies.
        available_copies (int): Number of available copies.
    """

    def __init__(self, book_id, title, author, isbn, total_copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies

    def is_available(self):
        """Returns True if at least one copy is available."""
        return self.available_copies > 0

    def borrow_copy(self):
        """Reduces available copies by one when borrowed."""
        if self.is_available():
            self.available_copies -= 1
            return True
        return False

    def return_copy(self):
        """Increases available copies by one when returned."""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def __str__(self):
        """Returns readable string of book details."""
        status = "Available" if self.is_available() else "Borrowed"
        return (f"[{self.book_id}] {self.title} by {self.author} "
                f"| ISBN: {self.isbn} | Status: {status} "
                f"| Copies: {self.available_copies}/{self.total_copies}")