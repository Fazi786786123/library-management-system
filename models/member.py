class Member:
    """
    Represents a library member.

    Attributes:
        member_id (str): Unique identifier for the member.
        name (str): Full name of the member.
        email (str): Email address of the member.
        is_active (bool): Whether the member is active.
        borrowed_books (list): List of book_ids currently borrowed.
    """

    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.is_active = True
        self.borrowed_books = []

    def borrow_book(self, book_id):
        """Adds book_id to borrowed list."""
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        """Removes book_id from borrowed list."""
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False

    def deactivate(self):
        """Deactivates the member account."""
        self.is_active = False

    def __str__(self):
        """Returns readable string of member details."""
        status = "Active" if self.is_active else "Inactive"
        return (f"[{self.member_id}] {self.name} "
                f"| Email: {self.email} | Status: {status} "
                f"| Borrowed: {len(self.borrowed_books)} book(s)")