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
        library_system.librarian_sign_in(self)

    def sign_in(self, library_system: LibrarySystem):
        library_system.librarian_sign_in(self)
        pass

    def set_password(self):
        pass

    def give_book(self):
        pass

    def accept_book(self):
        pass

    def add_books(self, books: List['Book']):
        self.library.add_books_db(books)

    def search_book(self):
        pass

    def remove_book(self):
        pass

    def update_catalog(self): # занести данные о том, что книга занята в бд
        pass

    def update_accounts(self):  # занести данные о взятых человеком книгах в бд
        pass



