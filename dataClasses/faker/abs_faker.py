from faker import Faker
import abc

from typing import TypeVar

T = TypeVar("T")

class AbsFaker(abc.ABC):

    _faker = Faker()

    def select_random(self, item_list:list[T]) -> T:
        _len = len(item_list)
        _index = self.generate_int(0, _len - 1)
        return item_list[_index]

    def generate_float(self, /, min :float = 0, max: float = 1) -> int:
        '''min and max are inclusive'''
        return self._faker.pyfloat(min_value = min, max_value = max)
    
    def generate_int(self, min :int, max: int) -> int:
        '''min and max are inclusive'''
        return self._faker.pyint(min_value = min, max_value = max)

    def generate_name_first(self) -> str:
        return self._faker.first_name()
    
    def generate_name_first_male(self) -> str:
        return self._faker.first_name_male()
    
    def generate_name_first_female(self) -> str:
        return self._faker.first_name_female()

    def generate_name_last(self) -> str:
        return self._faker.last_name()

    def generate_street_name(self) -> str:
        return self._faker.street_name()
    
    def generate_city(self) -> str:
        return self._faker.city()
    
    def generate_ISBN13(self) -> str:
        return self._faker.isbn13()
    
    def generate_business_speak(self) -> str:
        return self._faker.bs()