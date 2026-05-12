from datetime import date, timedelta
from models.loan import Loan


class LoanService:
    """
    Handles all loan-related operations (borrow and return).

    Attributes:
        loans (dict): Dictionary storing all loans by loan_id.
        next_id (int): Counter for generating unique loan IDs.
    """

    def __init__(self):
        self.loans = {}
        self.next_id = 1

    def generate_loan_id(self):
        """Generates a unique loan ID."""
        loan_id = f"L{str(self.next_id).zfill(3)}"
        self.next_id += 1
        return loan_id

    def borrow_book(self, member, book):
        """
        Creates a loan when a member borrows a book.

        Args:
            member (Member): The member borrowing the book.
            book (Book): The book being borrowed.

        Returns:
            Loan or None: Loan object if successful, None if failed.
        """
        if not member.is_active:
            print("Member account is not active.")
            return None

        if not book.borrow_copy():
            print("No copies available.")
            return None

        loan_id = self.generate_loan_id()
        borrow_date = date.today()
        due_date = borrow_date + timedelta(days=Loan.LOAN_DURATION_DAYS)

        new_loan = Loan(loan_id, member.member_id, book.book_id,
                        borrow_date, due_date)

        self.loans[loan_id] = new_loan
        member.borrow_book(book.book_id)

        return new_loan

    def return_book(self, member, book, loan_id):
        """
        Closes a loan when a member returns a book.

        Args:
            member (Member): The member returning the book.
            book (Book): The book being returned.
            loan_id (str): ID of the loan to close.

        Returns:
            bool: True if returned successfully, False otherwise.
        """
        loan = self.loans.get(loan_id, None)

        if not loan:
            print("Loan not found.")
            return False

        if loan.status == "closed":
            print("This loan is already closed.")
            return False

        loan.close_loan()
        book.return_copy()
        member.return_book(book.book_id)

        return True

    def get_active_loans(self):
        """Returns all currently active loans."""
        return [loan for loan in self.loans.values()
                if loan.status == "active"]

    def get_overdue_loans(self):
        """Returns all overdue loans."""
        return [loan for loan in self.loans.values()
                if loan.is_overdue()]