import string
from typing import List

class LibrarySystem:
    def __init__(self, name: string, database: 'DataBase' = None):
        self.name = name
        self.database = database
        self.connected_accounts = []
        self.connected_librarians = []

    def account_sign_up(self, account: 'Account'):
        self.add_account_db(account)

    def account_sign_in(self, account: 'Account'):
        self.connected_accounts.append(account)

    def account_log_out(self, account: 'Account'):
        self.connected_accounts.remove(account)

    def librarian_sign_up(self, librarian: 'Librarian'):
        self.add_librarian_db(librarian)

    def librarian_sign_in(self, librarian: 'Librarian'):
        self.connected_librarians.append(librarian)

    def librarian_log_out(self, librarian: 'Librarian'):
        self.connected_librarians.remove(librarian)

    def verify_account(self):
        pass

    def confirm_password(self):
        pass

    def add_account_db(self, account: 'Account'):
        try:
            self.database.add_account(account=account)
        except ValueError as ve:
            print(ve.args)

    def add_librarian_db(self, librarian: 'Librarian'):
        try:
            self.database.add_librarian(librarian=librarian)
        except ValueError as ve:
            print(ve.args)

    def get_books(self):
        books = self.database.catalog
        return books

    def show_books(self):
        books = list(book.display_info() for book in self.database.catalog)
        return books

    def search_book(self, title: string = None, author: string = None):
        books = self.database.catalog
        for book in books:
            if (book.title == title) or (book.author == author):
                return [book, books[book]]
        return None

    def add_books_db(self, books: 'Book'):
        self.database.add_books(books)

    def remove_book_db(self, title: string = None, author: string = None):
        books = self.database.catalog
        for book in books:
            if (book.title == title) or (book.author == author):
                self.database.remove_book(book)
                print('---The book "{}" was successfully removed---\n\n'.format(book.title))
                return

    def update_account_db(self, account: 'Account'):
        for acc in self.connected_accounts:
            if acc.id == account.id:
                self.connected_accounts.remove(acc)
                self.connected_accounts.append(account)
        self.database.update_account(account)

    def update_catalog_db(self, book: 'Book'):
        self.database.update_account(book)
