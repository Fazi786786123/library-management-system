import unittest
from models.book import Book
from models.member import Member
from models.loan import Loan
from services.book_service import BookService
from services.member_service import MemberService
from services.loan_service import LoanService
from datetime import date, timedelta


class TestBook(unittest.TestCase):
    """Test cases for Book model."""

    def setUp(self):
        """Set up a book object before each test."""
        self.book = Book("B001", "Clean Code", "Robert Martin", "978-01", 2)

    def test_book_is_available_initially(self):
        """Book should be available when first created."""
        self.assertTrue(self.book.is_available())

    def test_borrow_copy_reduces_available_copies(self):
        """Borrowing should reduce available copies by 1."""
        self.book.borrow_copy()
        self.assertEqual(self.book.available_copies, 1)

    def test_return_copy_increases_available_copies(self):
        """Returning should increase available copies by 1."""
        self.book.borrow_copy()
        self.book.return_copy()
        self.assertEqual(self.book.available_copies, 2)

    def test_book_unavailable_when_all_copies_borrowed(self):
        """Book should be unavailable when all copies are borrowed."""
        self.book.borrow_copy()
        self.book.borrow_copy()
        self.assertFalse(self.book.is_available())

    def test_cannot_borrow_when_unavailable(self):
        """Borrowing should fail when no copies available."""
        self.book.borrow_copy()
        self.book.borrow_copy()
        result = self.book.borrow_copy()
        self.assertFalse(result)


class TestMember(unittest.TestCase):
    """Test cases for Member model."""

    def setUp(self):
        """Set up a member object before each test."""
        self.member = Member("M001", "Ali Hassan", "ali@gmail.com")

    def test_member_is_active_initially(self):
        """Member should be active when first created."""
        self.assertTrue(self.member.is_active)

    def test_borrow_book_adds_to_list(self):
        """Borrowing adds book_id to member borrowed list."""
        self.member.borrow_book("B001")
        self.assertIn("B001", self.member.borrowed_books)

    def test_return_book_removes_from_list(self):
        """Returning removes book_id from member borrowed list."""
        self.member.borrow_book("B001")
        self.member.return_book("B001")
        self.assertNotIn("B001", self.member.borrowed_books)

    def test_deactivate_member(self):
        """Deactivating sets is_active to False."""
        self.member.deactivate()
        self.assertFalse(self.member.is_active)

    def test_return_book_not_borrowed(self):
        """Returning a book not borrowed should return False."""
        result = self.member.return_book("B999")
        self.assertFalse(result)


class TestBookService(unittest.TestCase):
    """Test cases for BookService."""

    def setUp(self):
        """Set up a fresh BookService before each test."""
        self.book_service = BookService()

    def test_add_book_returns_book_object(self):
        """Adding a book should return a Book object."""
        book = self.book_service.add_book("Clean Code", "Robert Martin", "978-01")
        self.assertEqual(book.title, "Clean Code")

    def test_add_book_generates_unique_ids(self):
        """Each book added should have a unique ID."""
        book1 = self.book_service.add_book("Book One", "Author A", "111")
        book2 = self.book_service.add_book("Book Two", "Author B", "222")
        self.assertNotEqual(book1.book_id, book2.book_id)

    def test_get_book_returns_correct_book(self):
        """get_book should return the correct book by ID."""
        book = self.book_service.add_book("Clean Code", "Robert Martin", "978-01")
        found = self.book_service.get_book(book.book_id)
        self.assertEqual(found.title, "Clean Code")

    def test_get_book_returns_none_for_invalid_id(self):
        """get_book should return None for non existent ID."""
        result = self.book_service.get_book("B999")
        self.assertIsNone(result)

    def test_remove_book_deletes_book(self):
        """Removing a book should delete it from the system."""
        book = self.book_service.add_book("Clean Code", "Robert Martin", "978-01")
        self.book_service.remove_book(book.book_id)
        result = self.book_service.get_book(book.book_id)
        self.assertIsNone(result)

    def test_remove_book_returns_false_for_invalid_id(self):
        """Removing non existent book should return False."""
        result = self.book_service.remove_book("B999")
        self.assertFalse(result)

    def test_search_book_by_title(self):
        """Search should find books matching title keyword."""
        self.book_service.add_book("Clean Code", "Robert Martin", "978-01")
        results = self.book_service.search_book("clean")
        self.assertEqual(len(results), 1)

    def test_search_book_by_author(self):
        """Search should find books matching author keyword."""
        self.book_service.add_book("Clean Code", "Robert Martin", "978-01")
        results = self.book_service.search_book("robert")
        self.assertEqual(len(results), 1)

    def test_search_book_no_results(self):
        """Search should return empty list if nothing matches."""
        results = self.book_service.search_book("xyz123")
        self.assertEqual(len(results), 0)

    def test_get_all_books(self):
        """get_all_books should return all added books."""
        self.book_service.add_book("Book One", "Author A", "111")
        self.book_service.add_book("Book Two", "Author B", "222")
        all_books = self.book_service.get_all_books()
        self.assertEqual(len(all_books), 2)


class TestMemberService(unittest.TestCase):
    """Test cases for MemberService."""

    def setUp(self):
        """Set up a fresh MemberService before each test."""
        self.member_service = MemberService()

    def test_register_member_returns_member(self):
        """Registering a member should return a Member object."""
        member = self.member_service.register_member("Ali", "ali@gmail.com")
        self.assertEqual(member.name, "Ali")

    def test_register_member_generates_unique_ids(self):
        """Each member registered should have a unique ID."""
        m1 = self.member_service.register_member("Ali", "ali@gmail.com")
        m2 = self.member_service.register_member("Sara", "sara@gmail.com")
        self.assertNotEqual(m1.member_id, m2.member_id)

    def test_get_member_returns_correct_member(self):
        """get_member should return correct member by ID."""
        member = self.member_service.register_member("Ali", "ali@gmail.com")
        found = self.member_service.get_member(member.member_id)
        self.assertEqual(found.name, "Ali")

    def test_get_member_returns_none_for_invalid_id(self):
        """get_member should return None for non existent ID."""
        result = self.member_service.get_member("M999")
        self.assertIsNone(result)

    def test_deactivate_member(self):
        """Deactivating a member should set is_active to False."""
        member = self.member_service.register_member("Ali", "ali@gmail.com")
        self.member_service.deactivate_member(member.member_id)
        self.assertFalse(member.is_active)


class TestLoanService(unittest.TestCase):
    """Test cases for LoanService."""

    def setUp(self):
        """Set up fresh services and objects before each test."""
        self.loan_service = LoanService()
        self.book = Book("B001", "Clean Code", "Robert Martin", "978-01", 2)
        self.member = Member("M001", "Ali Hassan", "ali@gmail.com")

    def test_borrow_book_creates_loan(self):
        """Borrowing a book should create and return a Loan object."""
        loan = self.loan_service.borrow_book(self.member, self.book)
        self.assertIsNotNone(loan)

    def test_borrow_book_reduces_available_copies(self):
        """Borrowing should reduce available copies."""
        self.loan_service.borrow_book(self.member, self.book)
        self.assertEqual(self.book.available_copies, 1)

    def test_borrow_book_fails_for_inactive_member(self):
        """Borrowing should fail if member is inactive."""
        self.member.deactivate()
        loan = self.loan_service.borrow_book(self.member, self.book)
        self.assertIsNone(loan)

    def test_borrow_book_fails_when_no_copies(self):
        """Borrowing should fail when no copies are available."""
        self.book.available_copies = 0
        loan = self.loan_service.borrow_book(self.member, self.book)
        self.assertIsNone(loan)

    def test_return_book_closes_loan(self):
        """Returning a book should close the loan."""
        loan = self.loan_service.borrow_book(self.member, self.book)
        self.loan_service.return_book(self.member, self.book, loan.loan_id)
        self.assertEqual(loan.status, "closed")

    def test_return_book_increases_available_copies(self):
        """Returning should increase available copies."""
        loan = self.loan_service.borrow_book(self.member, self.book)
        self.loan_service.return_book(self.member, self.book, loan.loan_id)
        self.assertEqual(self.book.available_copies, 2)

    def test_get_active_loans(self):
        """get_active_loans should return only active loans."""
        self.loan_service.borrow_book(self.member, self.book)
        active = self.loan_service.get_active_loans()
        self.assertEqual(len(active), 1)

    def test_loan_due_date_is_14_days(self):
        """Loan due date should be 14 days after borrow date."""
        loan = self.loan_service.borrow_book(self.member, self.book)
        expected_due = date.today() + timedelta(days=14)
        self.assertEqual(loan.due_date, expected_due)


if __name__ == "__main__":
    unittest.main()