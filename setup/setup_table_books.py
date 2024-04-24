from dataClasses.faker import FakerBook
from sql import DataObjQueries

def setup_table_books(amount: int):
    _book_gen = FakerBook()
    _books = []
    for _ in range(amount):
        for _book in _book_gen.create_random_book():
            _books.append(_book)

    DataObjQueries.insert_many(_books)