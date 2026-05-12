from models.book import Book


class BookService:
    """
    Handles all book-related operations.

    Attributes:
        books (dict): Dictionary storing all books by book_id.
        next_id (int): Counter for generating unique book IDs.
    """

    def __init__(self):
        self.books = {}
        self.next_id = 1

    def generate_book_id(self):
        """Generates a unique book ID."""
        book_id = f"B{str(self.next_id).zfill(3)}"
        self.next_id += 1
        return book_id

    def add_book(self, title, author, isbn, total_copies=1):
        """
        Adds a new book to the library.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
            isbn (str): ISBN of the book.
            total_copies (int): Number of copies to add.

        Returns:
            Book: The newly created book object.
        """
        book_id = self.generate_book_id()
        new_book = Book(book_id, title, author, isbn, total_copies)
        self.books[book_id] = new_book
        return new_book

    def remove_book(self, book_id):
        """
        Removes a book from the library.

        Args:
            book_id (str): ID of the book to remove.

        Returns:
            bool: True if removed, False if not found.
        """
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False

    def get_book(self, book_id):
        """
        Finds a book by its ID.

        Args:
            book_id (str): ID of the book.

        Returns:
            Book or None: Book object if found, else None.
        """
        return self.books.get(book_id, None)

    def get_all_books(self):
        """Returns a list of all books."""
        return list(self.books.values())

    def search_book(self, query):
        """
        Searches books by title or author.

        Args:
            query (str): Search keyword.

        Returns:
            list: List of matching Book objects.
        """
        query_lower = query.lower()
        results = [
            book for book in self.books.values()
            if query_lower in book.title.lower()
            or query_lower in book.author.lower()
        ]
        return results