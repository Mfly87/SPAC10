
from typing import Callable

class QueryConditions():

    @staticmethod
    def qry_equal(column_name:str, column_value:any) -> str:
        return "%s = %s" % (column_name, column_value)
    
    @staticmethod
    def qry_not_equal(column_name:str, column_value:any) -> str:
        return "%s != %s" % (column_name, column_value)

    @staticmethod
    def qry_like(column_name:str, column_value:any) -> str:
        return "%s LIKE '%%%s%%'" % (column_name, column_value)
    
    @staticmethod
    def qry_less_than(column_name:str, column_value:any) -> str:
        return "%s < %s" % (column_name, column_value)
    
    @staticmethod
    def qry_less_than_or_equal(column_name:str, column_value:any) -> str:
        return "%s <= %s" % (column_name, column_value)
    
    @staticmethod
    def qry_greater_than(column_name:str, column_value:any) -> str:
        return "%s > %s" % (column_name, column_value)
    
    @staticmethod
    def qry_greater_than_or_equal(column_name:str, column_value:any) -> str:
        return "%s >= %s" % (column_name, column_value)
    
    @staticmethod
    def get_operator_func(operator: str) -> Callable[[str,any], str]:
        match operator:
            case "==":
                return QueryConditions.qry_equal
            case "!=":
                return QueryConditions.qry_not_equal
            case "<":
                return QueryConditions.qry_less_than
            case "<=":
                return QueryConditions.qry_less_than_or_equal
            case ">":
                return QueryConditions.qry_greater_than
            case ">=":
                return QueryConditions.qry_greater_than_or_equal
            case _:
                return QueryConditions.qry_like





    @staticmethod
    def qry_and(conditions: list[str]) -> str:
        return "(%s)" % (" AND ".join(conditions))
    
    @staticmethod
    def qry_or(conditions: list[str]) -> str:
        return "(%s)" % (" OR ".join(conditions))