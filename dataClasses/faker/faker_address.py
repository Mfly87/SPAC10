from .abs_faker import AbsFaker
from ..data_types import SQLDataAddress
from ..data_factory import SQLDataFactory

class FakerAddress(AbsFaker):

    def create_random_address(self) -> list[SQLDataAddress]:
        _type = self.generate_int(0,10)
        if _type == 0:
            return self.create_lettered_address()
        elif _type < 5:
            return self.create_standard_address()
        else:
            return self.create_appartment_address()

    def create_appartment_address(self) -> list[SQLDataAddress]:
        _floors = ["st","1","2","3","4"]
        _floor = self.select_random(_floors)

        _sides = ["tv","th"]
        _side = self.select_random(_sides)

        _street_address = self._create_street_address()
        _street_address += " %s %s" % (_floor, _side)

        return self._build_street_address(_street_address)
    
    def create_lettered_address(self,) -> list[SQLDataAddress]:
        _letters = "ABCD"
        _letter = self.select_random(_letters)
        
        _street_address = self._create_street_address()
        _street_address += _letter

        return self._build_street_address(_street_address)
    
    def create_standard_address(self):
        _street_address = self._create_street_address()
        return self._build_street_address(_street_address)

    def _create_street_address(self) -> str:
        _street = self.generate_street_name()
        _street_number = self.generate_int(1,100)

        return "%s %i" % (_street, _street_number)

    def _build_street_address(self, street_address:str) -> list[SQLDataAddress]:
        _factory:SQLDataFactory = SQLDataFactory()
        _args = ["SQLDataAddress", street_address]
        return  _factory.create_data_obj(*_args)