from .abs_faker import AbsFaker
from ..data_types import SQLDataName
from ..data_factory import SQLDataFactory

class FakerName(AbsFaker):

    def create_random_name(self) -> list[SQLDataName]:
        _name_first = self.generate_name_first()
        _name_last = self.generate_name_last()
        return self._create_name(_name_first, _name_last)

    def _create_name(self, _name_first:str, _name_last:str) -> list[SQLDataName]:
        _factory:SQLDataFactory = SQLDataFactory()
        _args = ["SQLDataName", _name_first, _name_last]
        return  _factory.create_data_obj(*_args)