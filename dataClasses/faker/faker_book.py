from .abs_faker import AbsFaker
from ..data_types import SQLDataBook
from ..data_factory import SQLDataFactory

from .faker_name import FakerName

import uuid

class FakerBook(AbsFaker):

    _fake_name = FakerName()

    def create_random_book(self) -> list[SQLDataBook]:
        _author = self._fake_name.create_random_name()[0]
        
        _tite = self.generate_business_speak()
        _year = self.generate_int(1980,2020)
        _isbn = self.generate_ISBN13()
        _quantity = self.generate_int(1,10)
        

        _factory:SQLDataFactory = SQLDataFactory()
        _args = ["SQLDataBook", _tite, _author, _year, _isbn, _quantity, _quantity]
        return  _factory.create_data_obj(*_args)