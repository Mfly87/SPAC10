from dataClasses import AbsSQLObj, SQLDataUser, SQLDataFactory

print("\n\n\n")

_factory = SQLDataFactory()

_name = None
_address = None
_user = None

_obj_list = _factory.create_data_obj(*["SQLDataName", "John", "Doe"])
for _obj in _obj_list:
    _name = _obj

_obj_list = _factory.create_data_obj(*["SQLDataAddress", "Don Str 49"])
for _obj in _obj_list:
    _address = _obj

args = ["SQLDataUser", "sdfas", _name, _address, 45]
_obj_list = _factory.create_data_obj(*args)
for _obj in _obj_list:
    _user: SQLDataUser = _obj

print("\n\n\n")
print(_name)
print("")
print(_address)
print("")
print(_user)