from designPatterns import Singleton

from mysql.connector import MySQLConnection, Error

from ..queryGenerators import TableQueries

class DatabaseConnection(Singleton):

    _current_database = None
    _database_connector = None
        
    @property
    def database_connector(self) -> MySQLConnection:
        return self._database_connector
    
    @property
    def current_database(self):
        return self._current_database
    
    def connect_to_database(self, database_connector: MySQLConnection, database_name:str) -> None:
        self._database_connector: MySQLConnection = database_connector
        
        self.execute_querty(TableQueries.qry_create_database(database_name))
        self.execute_querty(TableQueries.qry_use_database(database_name))
        self._current_database = database_name

    def execute_many(self, query: str, parameters: list[tuple]) -> bool:
        try:
            with self.database_connector.cursor() as cursor:
                cursor.executemany(query, parameters)
                self.database_connector.commit()
                return True
        except Error as e:
            print(f"An error occured during an execute query {e}")
            return False

    def execute_querty(self, query: str) -> bool:
        try:
            with self.database_connector.cursor() as cursor:
                cursor.execute(query)
                self.database_connector.commit()
                return True
        except Error as e:
            print(f"An error occured during an execute query {e}")
            return False
        
    def execute_fetch_querty(self, _query: str) -> list[dict]:
        try:
            with self.database_connector.cursor(dictionary=True) as cursor:
                cursor.execute(_query)
                return cursor.fetchall()
        except Error as e:
            print(f"An error occured during a fetch query {e}")
            return []



    def get_table_names(self) -> list[str]:
        _query = TableQueries.qry_show_tables()
        _result: list[dict[str,str]] = self.execute_fetch_querty(_query)

        _name_list: list[str] = []
        for _dict in _result:
            for _value in _dict.values():
                _name_list.append(_value)
        return _name_list