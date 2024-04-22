from ..abstract import AbsSQLObj
from ..guard_functions import str_non_empty

class SQLDataName(AbsSQLObj):
        
    _first_name = None
    _last_name = None

    def __init__(self, first_name:str, last_name:str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self) -> str:
        return self._first_name
    @first_name.setter
    def first_name(self, value) -> None:
        value = str_non_empty(value)
        if value is not None:
            self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name
    @last_name.setter
    def last_name(self, value) -> None:
        value = str_non_empty(value)
        if value is not None:
            self._last_name = value

    @property
    def full_name(self) -> str:
        return "%s %s" % (self.first_name, self.last_name)

    @staticmethod
    def get_headers():
        return [
            "first_name",
            "last_name",
        ]
    
    @staticmethod
    def get_types():
        return [
            str,
            str,
        ]
    
    def get_values(self):
        return [
            self.first_name,
            self.last_name,
        ]
    
    def to_string(self):
        return self.full_name