from dataClasses import AbsSQLObj,SQLDataName, SQLDataFactory

_factory = SQLDataFactory()
print(_factory.get_data_obj_name_list())

_obj_list = _factory.create_data_obj(*["SQLDataName", "John", "Doe"])
for _obj in _obj_list:
    print(_obj.to_string())
