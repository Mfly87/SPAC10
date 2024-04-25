from .abs_faker import AbsFaker
from ..data_types import SQLDataBook, SQLDataName
from ..data_factory import SQLDataFactory

from .faker_name import FakerName

from typing import Callable

import scipy.stats as stats

class FakerBook(AbsFaker):

    _fake_name = FakerName()

    def create_random_book(self) -> list[SQLDataBook]:

        _author = self._get_name()[0]
           
        _tite = self.generate_business_speak().capitalize()
        _year = self.generate_int(1980,2020)

        _isbn = self.generate_ISBN13()
        _quantity = self.generate_int(1,10)

        _cumulative = 0        
        for _letter in [_tite[0], _author.first_name[0], _author.last_name[0]]:
            if _letter == "G":
                _cumulative += 1
        _quantity += int((_cumulative + (_cumulative * _cumulative))/2)

        _factory:SQLDataFactory = SQLDataFactory()
        _args = ["SQLDataBook", _tite, _author, _year, _isbn, _quantity, _quantity]
        return  _factory.create_data_obj(*_args)
    
    def _get_name(self) -> list[SQLDataName]:
        _name_first = self._get_name_first()
        _name_last = self._get_name_last()
        return self._fake_name._create_name(_name_first, _name_last)
    
    def _get_name_first(self) -> str:
        _is_male = self.generate_float() < 0.9
        if _is_male:
            return self.generate_name_first_male()
        return self.generate_name_first_female()
    
    def _get_name_last(self) -> str:
        _has_one = self.generate_float() < 0.75
        _name_last = self.generate_name_last()
        if _has_one:
            return _name_last
        _name_last += " %s" % (self.generate_name_last())
        return _name_last


