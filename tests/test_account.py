import unittest
from entities.librarian import Librarian
from entities.database import DataBase
from entities.member import Member
from entities.library_system import LibrarySystem
from entities.book import Book


class TestAccount(unittest.TestCase):
    def init_system(self):
        # CREATE INSTANCES
        self.database = DataBase()
        self.library_system = LibrarySystem(name='library1', database=self.database)
        self.librarian = Librarian(name='librarian1')

        # LIBRARIAN SIGN UP AND SIGN IN
        self.librarian.sign_up(library_system=self.library_system)
        self.librarian.sign_in(library_system=self.library_system)

        # ADD BOOKS
        self.book1 = Book(title='Martin Eden', author='Jack London',
                     description='interesting description of Martin Eden')
        self.book2 = Book(title='The Financier', author='Theodore Dreiser',
                     description='interesting description of The Financier')
        self.book3 = Book(title='Pride and Prejudice', author='Jane Austen',
                     description='interesting description of Pride and Prejudice')
        self.book4 = Book(title='Naive. Super', author='Erlend Loe',
                     description='interesting description of Naive. Super')
        self.librarian.add_books([self.book1, self.book2, self.book3, self.book4])

        name = 'new member'
        self.member = Member(name=name)

        # MEMBER SIGN UP AND SIGN IN
        self.member.sign_up(library=self.library_system)
        self.member.sign_in(library=self.library_system)

    def test_search_book(self):
        self.init_system()
        title = 'Martin Eden'
        author = 'Jack London'
        found_book = self.member.account.search_book(title=title, author=author)
        self.assertIs(found_book[0], self.book1)

    def test_take_book(self):
        self.init_system()
        title = 'Martin Eden'
        author = 'Jack London'
        self.member.account.take_book(title=title, author=author)
        self.assertIn(self.book1.title, list(book.title for book in self.member.account.borrowed_books))

    def test_return_book(self):
        self.init_system()
        title = 'Martin Eden'
        author = 'Jack London'
        self.member.account.take_book(title=title, author=author)
        self.member.account.return_book(title=title, author=author)
        self.assertIn(self.book1.title, list(book.title for book in self.member.account.returned_books))
