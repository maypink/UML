from typing import List, Dict
from entities.librarian import Librarian


class DataBase:
    def __init__(self):
        self.accounts = []  # List[Account]
        self.librarians = []  # List[Librarian]
        self.catalog = {}  # Dict({Book: amount})

    def add_account(self, account: 'Account'):
        if account not in self.accounts:
            self.accounts.append(account)
        else:
            raise ValueError('This account is already registered in library\n\n')

    def add_librarian(self, librarian: Librarian):
        if librarian not in self.librarians:
            self.librarians.append(librarian)
        else:
            raise ValueError('This librarian is already registered in library\n\n')

    def add_books(self, books: List['Book']):
        for book in books:
            for k in self.catalog:
                if k == book:
                    self.catalog[k] += 1
                    continue
            self.catalog[book] = 1

    def update_account(self, account: 'Account'):
        for acc in self.accounts:
            if acc.id == account.id:
                self.accounts.remove(acc)
                self.accounts.append(account)

    def update_librarians(self):
        pass

    def update_catalog(self, book: 'Book'):
        for cur_book in self.catalog:
            if cur_book.id == book.id:
                self.catalog.remove(cur_book)
                self.catalog.append(book)

    def remove_book(self, book: 'Book'):
        for cur_book in self.catalog:
            if cur_book.id == book.id:
                del self.catalog[cur_book]
                return
