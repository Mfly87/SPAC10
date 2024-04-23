class QueryConditions():

    @staticmethod
    def qry_equals(column_name:str, column_value:str) -> str:
        return "%s = %s" % (column_name, column_value)
    
    @staticmethod
    def qry_like(column_name:str, column_value:str) -> str:
        return "%s LIKE %%%s%%" % (column_name, column_value)
    
    @staticmethod
    def qry_and(conditions: list[str]) -> str:
        return "(%s)" % (" AND ".join(conditions))
    
    @staticmethod
    def qry_or(conditions: list[str]) -> str:
        return "(%s)" % (" OR ".join(conditions))