import string
import datetime


class Book:
    def __init__(self, title: string, author: string, description: string,
                 is_taken: bool = False, reader_id: string = None, taken_time: datetime.date = None):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.is_taken = is_taken
        self.reader_id = reader_id
        self.taken_time = taken_time

    def display_info(self):
        return {'title': self.title,
                'author': self.author,
                'description': self.description}

