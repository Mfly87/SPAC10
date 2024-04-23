from .abs_queries import AbsQueries

class ItemQueries(AbsQueries):

    @staticmethod
    def qry_select_all(table_name: str ,* , column_names: list[str] = []) -> str:
        _column_search = "*" if len(column_names) == 0 else ItemQueries._parenthases_list(column_names)
        return "SELECT %s FROM %s" % (_column_search, table_name)

    @staticmethod
    def qry_select(table_name: str , condition: str ,* , column_names: list[str] = [] ) -> str:
        _base_query = ItemQueries.qry_select_all(table_name, column_names = column_names)
        return "%s WHERE %s" % (_base_query, condition)

    @staticmethod
    def qry_insert_into(table_name: str, column_dict: dict[str, any]) -> str:
        _names, _values = ItemQueries._column_dict_to_parenthases_lists(column_dict)
        return "INSERT INTO %s %s VALUES %s" % (table_name, _names, _values)
    
    @staticmethod
    def qry_insert_into_template(table_name: str, column_names: list[str]) -> str:
        _names = ItemQueries._parenthases_list(column_names)
        _values = ItemQueries._parenthases_list(["%s" for _ in column_names])
        return "INSERT INTO %s %s VALUES %s" % (table_name, _names, _values)

    @staticmethod
    def qry_update(table_name: str, column_dict: dict[str, any], condition: str) -> str:
        _updated_values = ["%s = %s" % (x, column_dict[x]) for x in column_dict]
        _updated_values_string = ", ".join(_updated_values)    
        return "UPDATE %s SET %s WHERE %s" % (table_name, _updated_values_string, condition)

    @staticmethod
    def qry_delete(table_name:str, condition: str) -> str:
        return "DELETE FROM %s WHERE %s" % (table_name, condition)
