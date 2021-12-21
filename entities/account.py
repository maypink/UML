import string
import random
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
        book = self.search_book(title=title, author=author)

        if book is None:
            print('---Book "{}" is not found---'.format(title))
            return
        books = self.library.get_books()
        book = book[0]
        if book not in books:
            print('---No such book in the library---')
        else:
            if book.is_taken:
                return
            book.is_taken = True
            self.borrowed_books.append(book)

            connected_librarians = self.library.connected_librarians
            librarian = random.choice(connected_librarians)
            librarian.give_book(account=self, book=book)

            print('---Book "{}" was successfully taken---'.format(book.title))

    def return_book(self, title: string, author: string):
        book = self.search_book(title=title, author=author)

        if book is None:
            print('---There is no "{}" book in the library---'.format(title))
            return
        books = self.library.get_books()
        book = book[0]
        if book not in books:
            print('---No such book in the library---\n\n')
        else:
            if not book.is_taken:
                print('---You ve mistaken, this book is not taken---')
            else:
                self.borrowed_books.remove(book)
                book.is_taken = False
                self.returned_books.append(book)

                connected_librarians = self.library.connected_librarians
                librarian = random.choice(connected_librarians)
                librarian.accept_book(account=self, book=book)

                print('---Book "{}" was successfully returned---\n\n'.format(book.title))
