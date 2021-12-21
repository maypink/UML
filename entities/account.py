import string
from typing import List


class Account:
    def __init__(self, name: string):
        self.id = hash(name)
        self.name = name
        self.borrowed_books = []
        self.returned_books = []
        self.fine_amount = 0
        self.library = None

    def sign_up(self, library: 'Library'):
        self.library = library
        library.add_account_db(self)

    def sign_in(self, library: 'Library'):
        self.library.account_sign_in(account=self)

    def search_book(self, title: string = None, author: string = None):
        return self.library.search_book(title, author)

    def take_book(self, title: string, author: string):
        book = self.search_book(title=title, author=author)[0]

        if book is None:
            return
        books = self.library.get_books()

        if book not in books:
            print('No such book in the library')
        else:
            if book.is_taken:
                return
            book.is_taken = True
            self.borrowed_books.append(book)
            self.library.update_account_db(self)
            self.library.update_catalog_db(book)
            print('Book was successfully taken')

    def return_book(self, title: string, author: string):
        book = self.search_book(title=title, author=author)[0]

        if book is None:
            return
        books = self.library.get_books()

        if book not in books:
            print('No such book in the library')
        else:
            if not book.is_taken:
                return
            self.borrowed_books.remove(book)
            book.is_taken = False
            self.returned_books.append(book)
            self.library.update_account_db(self)
            self.library.update_catalog_db(book)
            print('Book was successfully returned')

    def pay_fine(self):
        pass

