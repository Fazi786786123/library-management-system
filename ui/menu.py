class Menu:
    """
    Console-based user interface for the Library Management System.

    Attributes:
        book_service (BookService): Service for book operations.
        member_service (MemberService): Service for member operations.
        loan_service (LoanService): Service for loan operations.
    """

    def __init__(self, book_service, member_service, loan_service):
        self.book_service = book_service
        self.member_service = member_service
        self.loan_service = loan_service

    def display_main_menu(self):
        """Displays the main menu options."""
        print("\n" + "=" * 40)
        print("    Library Management System")
        print("=" * 40)
        print("1. Book Menu")
        print("2. Member Menu")
        print("3. Loan Menu")
        print("4. Exit")
        print("=" * 40)

    def display_book_menu(self):
        """Displays book related options."""
        print("\n--- Book Menu ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. View All Books")
        print("5. Back")

    def display_member_menu(self):
        """Displays member related options."""
        print("\n--- Member Menu ---")
        print("1. Register Member")
        print("2. View All Members")
        print("3. Deactivate Member")
        print("4. Back")

    def display_loan_menu(self):
        """Displays loan related options."""
        print("\n--- Loan Menu ---")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. View Active Loans")
        print("4. View Overdue Loans")
        print("5. Back")

    # ── BOOK ACTIONS ──────────────────────────

    def handle_add_book(self):
        """Handles adding a new book."""
        print("\n-- Add Book --")
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        copies = input("Enter number of copies (default 1): ")
        total_copies = int(copies) if copies.isdigit() else 1
        book = self.book_service.add_book(title, author, isbn, total_copies)
        print(f"\nBook added successfully!\n{book}")

    def handle_remove_book(self):
        """Handles removing a book."""
        book_id = input("Enter Book ID to remove: ")
        if self.book_service.remove_book(book_id):
            print("Book removed successfully!")
        else:
            print("Book not found.")

    def handle_search_book(self):
        """Handles searching for a book."""
        query = input("Enter title or author to search: ")
        results = self.book_service.search_book(query)
        if results:
            print(f"\n{len(results)} result(s) found:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def handle_view_all_books(self):
        """Displays all books in the library."""
        books = self.book_service.get_all_books()
        if books:
            print(f"\nTotal books: {len(books)}")
            for book in books:
                print(book)
        else:
            print("No books in library.")

    # ── MEMBER ACTIONS ────────────────────────

    def handle_register_member(self):
        """Handles registering a new member."""
        print("\n-- Register Member --")
        name = input("Enter name: ")
        email = input("Enter email: ")
        member = self.member_service.register_member(name, email)
        print(f"\nMember registered successfully!\n{member}")

    def handle_view_all_members(self):
        """Displays all registered members."""
        members = self.member_service.get_all_members()
        if members:
            print(f"\nTotal members: {len(members)}")
            for member in members:
                print(member)
        else:
            print("No members registered.")

    def handle_deactivate_member(self):
        """Handles deactivating a member."""
        member_id = input("Enter Member ID to deactivate: ")
        if self.member_service.deactivate_member(member_id):
            print("Member deactivated successfully!")
        else:
            print("Member not found.")

    # ── LOAN ACTIONS ──────────────────────────

    def handle_borrow_book(self):
        """Handles borrowing a book."""
        member_id = input("Enter Member ID: ")
        book_id = input("Enter Book ID: ")

        member = self.member_service.get_member(member_id)
        book = self.book_service.get_book(book_id)

        if not member:
            print("Member not found.")
            return
        if not book:
            print("Book not found.")
            return

        loan = self.loan_service.borrow_book(member, book)
        if loan:
            print(f"\nBook borrowed successfully!\n{loan}")

    def handle_return_book(self):
        """Handles returning a book."""
        member_id = input("Enter Member ID: ")
        book_id = input("Enter Book ID: ")
        loan_id = input("Enter Loan ID: ")

        member = self.member_service.get_member(member_id)
        book = self.book_service.get_book(book_id)

        if not member:
            print("Member not found.")
            return
        if not book:
            print("Book not found.")
            return

        if self.loan_service.return_book(member, book, loan_id):
            print("Book returned successfully!")

    def handle_view_active_loans(self):
        """Displays all active loans."""
        loans = self.loan_service.get_active_loans()
        if loans:
            print(f"\nActive loans: {len(loans)}")
            for loan in loans:
                print(loan)
        else:
            print("No active loans.")

    def handle_view_overdue_loans(self):
        """Displays all overdue loans."""
        loans = self.loan_service.get_overdue_loans()
        if loans:
            print(f"\nOverdue loans: {len(loans)}")
            for loan in loans:
                print(loan)
        else:
            print("No overdue loans.")

    # ── MENU RUNNERS ──────────────────────────

    def run_book_menu(self):
        """Runs the book sub-menu loop."""
        while True:
            self.display_book_menu()
            choice = input("Enter choice: ")
            if choice == "1":
                self.handle_add_book()
            elif choice == "2":
                self.handle_remove_book()
            elif choice == "3":
                self.handle_search_book()
            elif choice == "4":
                self.handle_view_all_books()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Try again.")

    def run_member_menu(self):
        """Runs the member sub-menu loop."""
        while True:
            self.display_member_menu()
            choice = input("Enter choice: ")
            if choice == "1":
                self.handle_register_member()
            elif choice == "2":
                self.handle_view_all_members()
            elif choice == "3":
                self.handle_deactivate_member()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again.")

    def run_loan_menu(self):
        """Runs the loan sub-menu loop."""
        while True:
            self.display_loan_menu()
            choice = input("Enter choice: ")
            if choice == "1":
                self.handle_borrow_book()
            elif choice == "2":
                self.handle_return_book()
            elif choice == "3":
                self.handle_view_active_loans()
            elif choice == "4":
                self.handle_view_overdue_loans()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Try again.")

    def run(self):
        """Runs the main menu loop."""
        print("Welcome to the Library Management System!")
        while True:
            self.display_main_menu()
            choice = input("Enter choice: ")
            if choice == "1":
                self.run_book_menu()
            elif choice == "2":
                self.run_member_menu()
            elif choice == "3":
                self.run_loan_menu()
            elif choice == "4":
                print("\nGoodbye! Thank you for using the Library System.")
                break
            else:
                print("Invalid choice. Try again.")