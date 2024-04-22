from inspect import getmembers, isclass, isabstract
from .abstract import AbsSQLObj
from . import data_types

class SQLDataFactory():
    _data_obj_dict: dict[str,str] = {}
        
    def __init__(self) -> None:
        self._loadProducts()

    def _loadProducts(self):
        classes = getmembers(data_types, lambda m: isclass(m) and not isabstract(m) )
        
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, AbsSQLObj):
                self._data_obj_dict.update([[name, _type]])
    
    def get_data_obj_name_list(self) -> list[str]:
        '''
        Creates a list containing the names of all objects the factory can build
        '''

        _list = []
        for _data_obj_name in self._data_obj_dict:
            _list.append(_data_obj_name)
        return _list
    
    def create_data_obj(self, *args) -> list[AbsSQLObj]:
        '''
        First argument is the class name\n
        The following arguments are what's required to build the object
        '''

        _obj = self._build_data_obj(*args)
        if _obj is None:
            return []
        
        return [_obj]



    def _build_data_obj(self, *args) -> AbsSQLObj | None:
        _len_recieved = len(args)

        _class_name = args[0]
        _class_args = args[1:]

        _return_class: AbsSQLObj = self._data_obj_dict.get(_class_name, None)
        if _return_class is None:
            return None
        
        _len_required = len(AbsSQLObj.get_build_types(_return_class))
        
        if _len_required != _len_recieved:
            return None

        _return_obj = _return_class(*_class_args)
        return _return_obj