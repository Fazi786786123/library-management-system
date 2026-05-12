from datetime import date

class Loan:
    """
    Represents a loan record when a member borrows a book.

    Attributes:
        loan_id (str): Unique identifier for the loan.
        member_id (str): ID of the member who borrowed.
        book_id (str): ID of the borrowed book.
        borrow_date (date): Date the book was borrowed.
        due_date (date): Date the book must be returned.
        return_date (date): Actual return date (None if not returned).
        status (str): active or closed.
    """

    LOAN_DURATION_DAYS = 14

    def __init__(self, loan_id, member_id, book_id, borrow_date, due_date):
        self.loan_id = loan_id
        self.member_id = member_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = None
        self.status = "active"

    def close_loan(self):
        """Closes the loan when book is returned."""
        self.return_date = date.today()
        self.status = "closed"

    def is_overdue(self):
        """Returns True if loan is overdue."""
        if self.status == "active":
            return date.today() > self.due_date
        return False

    def __str__(self):
        """Returns readable string of loan details."""
        return (f"[{self.loan_id}] Member: {self.member_id} "
                f"| Book: {self.book_id} "
                f"| Borrowed: {self.borrow_date} "
                f"| Due: {self.due_date} "
                f"| Status: {self.status}")