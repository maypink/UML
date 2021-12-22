from entities.account import Account
from entities.book import Book
from entities.database import DataBase
from entities.librarian import Librarian
from entities.library_system import LibrarySystem
from entities.member import Member


if __name__ == '__main__':

    # CREATE INSTANCES
    database = DataBase()
    library_system = LibrarySystem(name='library1', database=database)
    librarian = Librarian(name='librarian1')

    # LIBRARIAN SIGN UP AND SIGN IN
    librarian.sign_up(library_system=library_system)
    librarian.sign_in(library_system=library_system)
    print('connected librarians: {}\n\n'.format(library_system.connected_librarians[0].name))

    # ADD BOOKS
    book1 = Book(title='Martin Eden', author='Jack London',
                 description='interesting description of Martin Eden')
    book2 = Book(title='The Financier', author='Theodore Dreiser',
                 description='interesting description of The Financier')
    book3 = Book(title='Pride and Prejudice', author='Jane Austen',
                 description='interesting description of Pride and Prejudice')
    book4 = Book(title='Naive. Super', author='Erlend Loe',
                 description='interesting description of Naive. Super')
    librarian.add_books([book1, book2, book3, book4])
    print('----Books found in the {}: \n{}----\n\n'.format(librarian.library.name, librarian.library.get_books()))

    print('Enter your name to sign up in the library')
    name = str(input())
    member = Member(name=name)

    # MEMBER SIGN UP AND SIGN IN
    member.sign_up(library=library_system)
    member.sign_in(library=library_system)

    while True:
        print('Press:\n'
              '0 -- to search for book\n'
              '1 -- to take book\n'
              '2 -- to return book\n'
              '3 -- to show books that are in use now\n'
              '4 -- to show returned books\n')
        a = int(input())

        if a == 0:
            # BOOK SEARCH
            print("Enter book title or author of book or both")
            print("Title: ")
            title = str(input())
            print("Author: ")
            author = str(input())

            found_book = member.account.search_book(title=title, author=author)
            if found_book is not None:
                print('----Found book {} in {} copies----\n\n'.format(found_book[0].title, found_book[1]))
            else:
                print('---There is no "{}" {} book in the library---'.format(title, author))

        if a == 1:
            # TAKE BOOK
            print("Enter book title or author of book or both")
            print("Title: ")
            title = str(input())
            print("Author: ")
            author = str(input())
            member.account.take_book(title=title, author=author)

        if a == 2:
            # RETURN BOOK
            print("Enter book title or author of book or both")
            print("Title: ")
            title = str(input())
            print("Author: ")
            author = str(input())
            member.account.return_book(title=title, author=author)

        if a == 3:
            print('Books that are now in use: ', list(book.title for book in member.account.borrowed_books))

        if a == 4:
            print('Returned books: ', list(book.title for book in member.account.returned_books))

        if a == -10:
            print("Goodbye")
            break



