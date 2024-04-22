from ..abstract import AbsSQLObj
from ..guard_functions import str_non_empty

class SQLDataAddress(AbsSQLObj):

    _street_address = None

    def __init__(self, street_address:str) -> None:
        self.street_address = street_address

    @property
    def street_address(self) -> str:
        return self._street_address
    @street_address.setter
    def street_address(self, value) -> None:
        value = str_non_empty(value)
        if value is not None:
            self._street_address = value

    @staticmethod
    def get_headers():
        return [
            "street_address",
        ]
    
    @staticmethod
    def get_types():
        return [
            str,
        ]
    
    def get_values(self):
        return [
            self.street_address,
        ]
    
    def to_string(self):
        return self.street_address
