from dataClasses import AbsSQLObj

from ..queryGenerators import TableQueries, ItemQueries
from ..sqlConnection import DatabaseConnection

class DataQueries():

    _database_connection = DatabaseConnection()        

    @property
    def database_connection(self) -> DatabaseConnection:
        return self._database_connection

    def create_table(self, obj_type: type) -> None:
        if not issubclass(obj_type, AbsSQLObj):
            return
        
        _headers = AbsSQLObj.get_build_headers(obj_type)
        _types = AbsSQLObj.get_build_types(obj_type)
        _dict = dict(zip(_headers, _types))

        _name = self._get_table_name(obj_type)
        
        self._create_table(_name, _dict)

    def insert_many(self, objs: list[AbsSQLObj]) -> None:
        if not objs:
            return

        _type = type(objs[0])
        if not issubclass(_type, AbsSQLObj):
            return

        _name = self._get_table_name(_type)

        _headers = AbsSQLObj.get_build_headers(_type)
        _values = [x.get_build_values() for x in objs]
        
        _query = ItemQueries.qry_insert_into_template(_name, _headers)
        self.database_connection.execute_many(_query, _values)











    def _create_table(self, table_name:str, column_type_dict: dict[str, type]):
        self.database_connection.execute_querty(TableQueries.qry_drop_table(table_name))
        self.database_connection.execute_querty(TableQueries.qry_create_table(table_name, column_type_dict))

    def _get_table_name(self, value: any) -> str:
        if not isinstance(value, str):
            if not isinstance(value, type):
                value = type(value)
            value = value.__name__
        return value.lower()
    
