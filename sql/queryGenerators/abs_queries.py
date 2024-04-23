import abc

class AbsQueries():

    @staticmethod
    def _column_dict_to_parenthases_lists(column_dict: dict[str, any]) -> tuple[str, str]:
        _names = AbsQueries._parenthases_list(column_dict.keys())
        _values = AbsQueries._parenthases_list(column_dict.values())
        return (_names, _values)

    @staticmethod
    def _parenthases_list(item_list: list[any]) -> str:
        item_list = [str(x) for x in item_list]
        return "(%s)" % (", ".join(item_list))