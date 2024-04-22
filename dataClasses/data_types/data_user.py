from ..abstract import AbsSQLObj

from .data_name import SQLDataName
from .data_address import SQLDataAddress

from ..guard_functions import str_non_empty, int_is_zero_or_greater, is_sub_class

class SQLDataUser(AbsSQLObj):

    _id = None
    _name = None
    _address = None
    _privileges = None

    def __init__(self, id:str, name:SQLDataName, address:SQLDataAddress, privileges:int) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.privileges = privileges

    @property
    def id(self) -> str:
        return self._id
    @id.setter
    def id(self, value) -> None:
        value = str_non_empty(value)
        if value is not None:
            self._id = value

    @property
    def name(self) -> SQLDataName:
        return self._name
    @name.setter
    def name(self, value) -> None:
        if is_sub_class(value, SQLDataName):
            self._name = value

    @property
    def address(self) -> SQLDataAddress:
        return self._address
    @address.setter
    def address(self, value) -> None:
        if is_sub_class(value, SQLDataAddress):
            self._address = value

    @property
    def privileges(self) -> int:
        return self._privileges
    @privileges.setter
    def privileges(self, value) -> None:
        value = int_is_zero_or_greater(value)
        if value is not None:
            self._privileges = value


    @staticmethod
    def get_headers():
        return [
            "id",
            "name",
            "address",
            "privileges",
        ]
    
    @staticmethod
    def get_types():
        return [
            str,
            SQLDataName,
            SQLDataAddress,
            int
        ]
    
    def get_values(self):
        return [
            self.id,
            self.name,
            self.address,
            self.privileges,
        ]
    
    def to_string(self):
        return "%s (%s) (%s) %s"%(
            self.id,
            self.name,
            self.address,
            self.privileges
        )
