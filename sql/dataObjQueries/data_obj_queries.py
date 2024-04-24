from dataClasses import AbsSQLObj

from ..queryGenerators import TableQueries, ItemQueries
from ..sqlConnection import DatabaseConnection

class DataObjQueries():
    '''
    _database_connection = DatabaseConnection()        

    @property
    def database_connection(self) -> DatabaseConnection:
        return self._database_connection
    '''

    @staticmethod
    def create_table(obj_type: type) -> None:
        if not issubclass(obj_type, AbsSQLObj):
            return
        
        _headers = AbsSQLObj.get_build_headers(obj_type)[1:]
        _types = AbsSQLObj.get_build_types(obj_type)[1:]
        _dict = dict(zip(_headers, _types))

        _name = DataObjQueries._get_table_name(obj_type)
        
        DataObjQueries._create_table(_name, _dict)

    @staticmethod
    def insert_many(objs: list[AbsSQLObj]) -> None:
        if not objs:
            return

        _type = type(objs[0])
        if not issubclass(_type, AbsSQLObj):
            return

        _name = DataObjQueries._get_table_name(_type)

        _headers = AbsSQLObj.get_build_headers(_type)[1:]
        _values = [DataObjQueries._get_lower_values(x)[1:] for x in objs]

        _query = ItemQueries.qry_insert_into_template(_name, _headers)

        _connection:DatabaseConnection = DatabaseConnection()
        _connection.execute_many(_query, _values)

    @staticmethod
    def _get_lower_values(obj: AbsSQLObj) -> list[any]:
        _list = []
        for _value in obj.get_build_values():
            if isinstance(_value, str):
                _value = _value.lower()
            _list.append(_value)
        return _list

    @staticmethod
    def fetch(data_type: type, condition: str) -> list[dict]:
        if not issubclass(data_type, AbsSQLObj):
            return
        _name = DataObjQueries._get_table_name(data_type)
        
        _query = ItemQueries.qry_select(_name, condition)
        
        _connection:DatabaseConnection = DatabaseConnection()
        return _connection.execute_fetch_querty(_query)








    @staticmethod
    def _create_table(table_name:str, column_type_dict: dict[str, type]):
        _connection:DatabaseConnection = DatabaseConnection()
        _connection.execute_querty(TableQueries.qry_drop_table(table_name))
        _connection.execute_querty(TableQueries.qry_create_table(table_name, column_type_dict))
    
    @staticmethod
    def _get_table_name(value: any) -> str:
        if not isinstance(value, str):
            if not isinstance(value, type):
                value = type(value)
            value = value.__name__
        return value.lower()
    
