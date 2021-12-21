from entities.account import Account
from entities.book import Book
from entities.database import DataBase
from entities.librarian import Librarian
from entities.library_system import LibrarySystem
from entities.member import Member


if __name__ == '__main__':
    # a = -1
    # while a != 2:
    #     print('Добро пожаловать!'
    #           'Нажмите:'
    #           '0 -- создать базу данных для библиотеки'
    #           '1 -- создать информационную систему библиотеки'
    #           '2 -- создать и зарегистрировать нового библиотекаря'
    #           '3 -- создать и зарегистрировать новый аккаунт'
    #           '4 -- создать новую книгу и добавить ее'
    #           '5 -- ')
    #     a = int(input())
    #     if a == 0:
    #         print('b')
    #     if a == 1:
    #         print('a')
    #     if a == 2:
    #         print('c')
    #         break

    # CREATE INSTANCES
    database = DataBase()
    library_system = LibrarySystem(name='library1', database=database)
    librarian = Librarian(name='librarian1')
    member1 = Member(name='member1')

    # LIBRARIAN SIGN UP AND SIGN IN
    librarian.sign_up(library_system=library_system)
    librarian.sign_in(library_system=library_system)
    print('connected librarians: ', library_system.connected_librarians[0].name)

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
    print('----Books found in the {}: \n{}----'.format(librarian.library.name, librarian.library.get_books()))

    # MEMBER SIGN UP AND SIGN IN
    member1.sign_up(library=library_system)
    member1.sign_in(library=library_system)

    # BOOK SEARCH
    found_book = member1.account.search_book(book1.title)
    print('----Found book {} in {} copies----'.format(found_book[0].title, found_book[1]))

    # TAKE BOOK
    member1.account.take_book(title=book2.title, author=book2.author)
    member1.account.take_book(title=book3.title, author=book3.author)
    print(member1.account.borrowed_books)

    # RETURN BOOK
    member1.account.return_book(title=book2.title, author=book2.author)
    print('Books that are now in use: ', member1.account.borrowed_books)
    print('Returned books: ', member1.account.returned_books)




