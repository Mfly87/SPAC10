from dataClasses.faker import FakerBook
from sql import DataObjQueries

import json

def setup_table_books():
    
    _faker_book_amount = ""

    with open('config.json') as f:
        _config: dict[str,any] = json.load(f)
        _faker_book_amount = _config.get("faker_book_amount", 0)

    _book_gen = FakerBook()
    _books = []
    for _ in range(_faker_book_amount):
        for _book in _book_gen.create_random_book():
            _books.append(_book)

    if not _books:
        return
    
    DataObjQueries.insert_many(_books)