from services.book_service import BookService
from services.member_service import MemberService
from services.loan_service import LoanService
from ui.menu import Menu


def main():
    """Entry point of the Library Management System."""
    book_service = BookService()
    member_service = MemberService()
    loan_service = LoanService()

    menu = Menu(book_service, member_service, loan_service)
    menu.run()


if __name__ == "__main__":
    main()