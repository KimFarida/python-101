#CREATE CUSTOM EXCEPTION

# Custom exceptions hierarchy
#The class LibraryError inherits from the base class Exception
class LibraryError(Exception):
    """Base exception class for library operations"""

    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code
        self.timestamp = datetime.now()


#ASSIGNMENT
class BookError(LibraryError):
    """Base exception for book-related errors"""
    pass


class UserError(LibraryError):
    """Base exception for user-related errors"""
    pass


class BookNotFoundError(BookError):
    """Raised when a book cannot be found"""

    def __init__(self, isbn, message=None):
        self.isbn = isbn
        super().__init__(
            message or f"Book with ISBN {isbn} not found",
            error_code="BK404"
        )

# except  BookUnavailableError("1988", "This book has been boroowed") as e:
#    print(e)
class BookUnavailableError(BookError):
    """Raised when a book exists but cannot be borrowed"""

    def __init__(self, isbn, reason):
        self.isbn = isbn
        self.reason = reason
        super().__init__(
            f"Book {isbn} is unavailable: {reason}",
            error_code="BK503"
        )


"""
#is this user in our libary?

try:
    libary.lendbooK(user_id)
except UserBannedError as e:
    print(e)
except OverdueEroor as e:
    print e
except  BookUnavailableError(user_id, current_count, max_Allowed) as e:
    print(e)
"""
class BookLimitExceededError(UserError):
    """Raised when user tries to borrow more books than allowed"""

    def __init__(self, user_id, current_count, max_allowed):
        self.user_id = user_id
        self.current_count = current_count
        self.max_allowed = max_allowed
        super().__init__(
            f"User {user_id} cannot borrow more books. "
            f"Current: {current_count}, Maximum: {max_allowed}",
            error_code="USR429"
        )


class UserBannedError(UserError):
    """Raised when banned user tries to perform an action"""

    def __init__(self, user_id, ban_reason, ban_expiry=None):
        self.user_id = user_id
        self.ban_reason = ban_reason
        self.ban_expiry = ban_expiry
        message = f"User {user_id} is banned: {ban_reason}"
        if ban_expiry:
            message += f" (until {ban_expiry})"
        super().__init__(message, error_code="USR403")


class OverdueError(UserError):
    """Raised when user has overdue books"""

    def __init__(self, user_id, overdue_books):
        self.user_id = user_id
        self.overdue_books = overdue_books
        book_list = ", ".join(f"{book['title']} (due: {book['due_date']})"
                              for book in overdue_books)
        super().__init__(
            f"User {user_id} has overdue books: {book_list}",
            error_code="USR402"
        )


# Example library management class using these exceptions
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import logging


class Library:
    def __init__(self):
        self.books: Dict[str, dict] = {}
        self.users: Dict[int, dict] = {}
        self.loans: Dict[str, dict] = {}
        self.max_books_per_user = 5
        self.logger = logging.getLogger(__name__)

    def add_book(self, isbn: str, title: str, copies: int = 1) -> None:
        """Add a book to the library inventory"""
        if isbn in self.books:
            self.books[isbn]['copies'] += copies
        else:
            self.books[isbn] = {
                'title': title,
                'copies': copies,
                'available': copies
            }

    def check_user_status(self, user_id: int) -> None:
        """Verify user can perform operations"""
        if user_id not in self.users:
            raise UserError(f"User {user_id} not registered", "USR404")

        user = self.users[user_id]

        if user.get('banned'):
            raise UserBannedError(
                user_id,
                user['ban_reason'],
                user.get('ban_expiry')
            )

        # Check for overdue books
        overdue_books = [
            {
                'title': self.books[loan['isbn']]['title'],
                'due_date': loan['due_date']
            }
            for loan in self.loans.values()
            if loan['user_id'] == user_id
               and loan['due_date'] < datetime.now()
        ]

        if overdue_books:
            raise OverdueError(user_id, overdue_books)

    def borrow_book(self, user_id: int, isbn: str) -> datetime:
        """Attempt to borrow a book"""
        try:
            self.check_user_status(user_id)

            # Check book exists
            if isbn not in self.books:
                raise BookNotFoundError(isbn)

            # Check book availability
            if self.books[isbn]['available'] <= 0:
                raise BookUnavailableError(isbn, "All copies are borrowed")

            # Check user's book limit
            user_loans = sum(
                1 for loan in self.loans.values()
                if loan['user_id'] == user_id
            )

            if user_loans >= self.max_books_per_user:
                raise BookLimitExceededError(
                    user_id,
                    user_loans,
                    self.max_books_per_user
                )

            # Process the loan
            #loan dict, key is loan_id
            loan_id = f"{isbn}-{user_id}-{datetime.now().timestamp()}" #"BK156-USR145-1729424905.830923"
            due_date = datetime.now() + timedelta(days=14)

            self.loans[loan_id] = {
                'user_id': user_id,
                'isbn': isbn,
                'borrowed_date': datetime.now(),
                'due_date': due_date
            }

            # "BK156-USR145-1729424905.830923" : {
            #   'user_id': "USR145",
            #   'isbn': "BK156",
            #   'borrowed_date': datetime.datetime(2024, 10, 20, 12, 48, 6, 343321)
            #   'due_date': datetime.datetime(2024, 11, 3, 12, 51, 51, 48600)
            # }

            # key = None
            # for loan in loan_dict.items():
            # if loan[user_id] == userid and loan[isbn] == isbn:
            #   key = loan
            #   break
            # loan_Dict.pop(key)

            self.books[isbn]['available'] -= 1
            return due_date

        except LibraryError as e:
            self.logger.error(f"Failed to borrow book: {e}", exc_info=True)
            raise
        except Exception as e:
            self.logger.critical("Unexpected error during book borrowing", exc_info=True)
            raise LibraryError("System error occurred") from e

    def return_book(self, user_id: int, isbn: str) -> None:
        """Return a borrowed book"""
        try:
            # Find the loan record
            loan_id = next(
                (lid for lid, loan in self.loans.items()
                 if loan['user_id'] == user_id and loan['isbn'] == isbn),
                None
            )

            if not loan_id:
                raise LibraryError(
                    f"No active loan found for user {user_id} and book {isbn}",
                    "LN404"
                )

            # Process return
            del self.loans[loan_id]
            self.books[isbn]['available'] += 1

            # Check if book was overdue
            if self.loans[loan_id]['due_date'] < datetime.now():
                self.logger.warning(f"Book {isbn} returned late by user {user_id}")
                return False
            return True

        except Exception as e:
            self.logger.error(f"Error returning book: {e}", exc_info=True)
            raise


# Example usage and error handling
def main():
    library = Library()

    try:
        # Add some books
        library.add_book("123456789", "Python Programming", 2)
        library.add_book("987654321", "Data Structures", 1)

        # Try to borrow books
        try:
            library.users[12345] = {
                    'id': 12345,
                    'name': 'Jane Doe',
                    'email': 'jane@example.com',
                    'membership_type': 'standard',  # standard, premium, student, etc.
                    'joined_date': datetime(2024, 1, 15),
                    'banned': True,
                    'ban_reason': "Late return",
                    'ban_expiry': datetime(2024, 11, 3, 12, 51, 51, 48600),
                    'current_loans': [],
                    'loan_history': [],
                    'fines': 0.0,
                    'max_loans': 5,
                    'notifications': {
                        'email': True,
                        'sms': False
        },
        'last_activity': datetime(2024, 3, 15)  # Last borrowing/returning activity
        }
            due_date = library.borrow_book(12345, "123456789")
            print(f"Book borrowed successfully! Due date: {due_date}")
        except BookNotFoundError as e:
            print(f"Error {e.error_code}: {e}")
        except BookUnavailableError as e:
            print(f"Error {e.error_code}: {e}")
        except UserError as e:
            print(f"User error {e.error_code}: {e}")
            if isinstance(e, OverdueError):
                print("Overdue books:", e.overdue_books)
            elif isinstance(e, UserBannedError):
                print(f"Ban expires: {e.ban_expiry}")

    except LibraryError as e:
        print(f"Library error occurred: {e}")
        print(f"Error code: {e.error_code}")
        print(f"Timestamp: {e.timestamp}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()