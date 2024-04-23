from ..abstract import AbsSQLObj

from .data_name import SQLDataName

from ..guard_functions import str_non_empty, int_is_zero_or_greater, is_sub_class

class SQLDataBook(AbsSQLObj):

    _title = None
    _author = None
    _year = None
    _isbn = None
    _quantity = None
    _quantity_available = None


    def __init__(self, title:str, author:SQLDataName, year:int, isbn:str, quantity:str, quantity_available:int) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.quantity = quantity
        self.quantity_available = quantity_available

    @property
    def title(self) -> str:
        return self._title
    @title.setter
    def title(self, value) -> None:
        value = str_non_empty(value)
        if value is not None:
            self._title = value

    @property
    def author(self) -> SQLDataName:
        return self._author
    @author.setter
    def author(self, value) -> None:
        if is_sub_class(value, SQLDataName):
            self._author = value

    @property
    def year(self) -> int:
        return self._year
    @year.setter
    def year(self, value) -> None:
        value = int_is_zero_or_greater(value)
        if value is not None:
            self._year = value

    @property
    def isbn(self) -> str:
        return self._isbn
    @isbn.setter
    def isbn(self, value) -> None:
        value = str_non_empty(value)
        if value is not None:
            self._isbn = value

    @property
    def quantity(self) -> int:
        return self._quantity
    @quantity.setter
    def quantity(self, value) -> None:
        value = int_is_zero_or_greater(value)
        if value is not None:
            self._quantity = value

    @property
    def quantity_available(self) -> int:
        return self._quantity_available
    @quantity_available.setter
    def quantity_available(self, value) -> None:
        value = int_is_zero_or_greater(value)
        if value is not None:
            self._quantity_available = value


    @staticmethod
    def get_headers():
        return [
            "title",
            "author",
            "year",
            "ISBN",
            "quantity",
            "quantity_available",
        ]
    
    @staticmethod
    def get_types():
        return [
            str,
            SQLDataName,
            int,
            str,
            int,
            int
        ]
    
    def get_values(self):
        return [
            self.title,
            self.author,
            self.year,
            self.isbn,
            self.quantity,
            self.quantity_available,
        ]
    
    def to_string(self):
        return "%s (%s) %s %s qty: %s"%(
            self.title,
            self.author,
            self.year,
            self.isbn,
            self.quantity,
            self.quantity_available,
        )
