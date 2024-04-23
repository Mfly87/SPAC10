from .abs_queries import AbsQueries

class TableQueries(AbsQueries):
    
    @staticmethod
    def qry_use_database(table_name: str) -> str:
        return "USE %s" % (table_name)
    
    @staticmethod
    def qry_show_tables():
        return "SHOW TABLES"

    @staticmethod
    def qry_create_database(database_name: str) -> str:
        return "CREATE DATABASE IF NOT EXISTS %s" % (database_name)
    
    @staticmethod
    def qry_create_table(table_name: str, column_type_dict: dict[str, type]) -> str:
        _type_list = ["%s %s" % (x, TableQueries._type(column_type_dict[x])) for x in column_type_dict]
        _types = TableQueries._parenthases_list(_type_list)
        return "CREATE TABLE IF NOT EXISTS %s %s" % (table_name, _types)
    
    @staticmethod
    def qry_drop_table(table_name: str) -> str:
        return "DROP TABLE IF EXISTS %s" % (table_name)

    @staticmethod
    def _type(var: type) -> str:
        if var is int:
            return "int"
        return "varchar(255)"