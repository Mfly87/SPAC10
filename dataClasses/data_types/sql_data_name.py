from ..abstract import AbsSQLObj

class SQLDataName(AbsSQLObj):

    def __init__(self, first_name:str, last_name:str) -> None:
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def full_name(self) -> str:
        return "%s %s" % (self.first_name, self.last_name)
    
    def to_string(self):
        return self.full_name

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
