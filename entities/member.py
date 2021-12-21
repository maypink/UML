import string
from entities.account import Account


class Member:
    def __init__(self, name: string):
        self.name = name
        self.account = None

    def sign_up(self, library: 'Library'):
        self.account = Account(name=self.name)
        self.account.sign_up(library=library)

    def sign_in(self, library: 'Library'):
        self.account.sign_in(library=library)
