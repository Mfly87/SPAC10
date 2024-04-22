from .abs_faker import AbsFaker
from ..data_types import SQLDataUser, SQLDataAddress, SQLDataName
from ..data_factory import SQLDataFactory

from .faker_name import FakerName
from .faker_address import FakerAddress

import uuid

class FakerUser(AbsFaker):

    _fake_name = FakerName()
    _fake_address = FakerAddress()

    def create_random_user(self) -> list[SQLDataUser]:
        _name = self._fake_name.create_random_name()[0]
        _address = self._fake_address.create_random_address()[0]

        _uuid = str(uuid.uuid4())[:8]

        _factory:SQLDataFactory = SQLDataFactory()
        _args = ["SQLDataUser", _uuid, _name, _address, 0]
        return  _factory.create_data_obj(*_args)