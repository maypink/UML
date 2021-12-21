import string
from typing import List
from entities.library_system import LibrarySystem


class Librarian:
    def __init__(self, name: string):
        self.id = hash(name)
        self.name = name
        self.password = ''
        self.library = None

    def verify_account(self):
        pass

    def sign_up(self, library_system: LibrarySystem):
        self.library = library_system
        library_system.librarian_sign_up(self)

    def sign_in(self, library_system: LibrarySystem):
        library_system.librarian_sign_in(self)
        pass

    def set_password(self):
        pass

    def give_book(self, account: 'Account', book: 'Book'):
        self.update_accounts(account=account)
        self.update_catalog(book=book)

    def accept_book(self, account: 'Account', book: 'Book'):
        self.update_accounts(account=account)
        self.update_catalog(book=book)

    def add_books(self, books: List['Book']):
        self.library.add_books_db(books)

    def search_book(self, title: string = None, author: string = None):
        return self.library.search_book(title, author)

    def remove_book(self, title: string = None, author: string = None):
        self.library.remove_book_db(title=title, author=author)

    def update_catalog(self, book: 'Book'):  # занести данные о том, что книга занята в бд
        self.library.update_catalog_db(book)

    def update_accounts(self, account: 'Account'):  # занести данные о взятых человеком книгах в бд
        self.library.update_account_db(account=account)



