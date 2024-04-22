from inspect import getmembers, isclass, isabstract
from .abstract import AbsSQLObj
from . import data_types

from designPatterns import Singleton

class SQLDataFactory(Singleton):
    _data_obj_dict: dict[str,str] = {}
    _error_log = []

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

        args = self._unroll_args(*args)

        _obj = self._build_data_obj(*args)
        if _obj is None:
            return []
        
        return [_obj]





    def _unroll_args(self, *args):
        _index = len(args)

        while 0 < _index:
            _index -= 1
            _arg: AbsSQLObj = args[_index]
            
            if _arg is None:
                continue

            _type = type(_arg)
            if not issubclass(_type, AbsSQLObj):
                continue

            _values = _arg.get_values()
            
            _args_list = [*args]
            _args_list = _args_list[0:_index] + _values + _args_list[_index+1:]
            args = (_args_list)
            
        return args

    def _enroll_args(self, type_list: list[any], *args):
        _min_len = min( len(type_list), len(args) )

        _index = 0
        while _index + 1 < _min_len:
            _index += 1
            _arg: AbsSQLObj = args[_index]
            
            if _arg is None:
                continue

            _type = type_list[_index - 1]
            if not issubclass(_type, AbsSQLObj):
                continue

            _sub_index_len = len(_type.get_types())
            
            _main_list, _sub_list = self._split_list([*args], _index, _sub_index_len)
            _sub_list.insert(0, _type.__name__)

            _obj = self._build_data_obj(*_sub_list)
            _main_list.insert(_index, _obj)


            args = (_main_list)
        return args
            
        
    def _split_list(self, main_list: list[any], start_index: int, len:int) -> tuple[list[any],list[any]]:
        _end_index = start_index + len
        _sub_list = main_list[start_index:_end_index]
        _main_list = main_list[:start_index] + main_list[_end_index:]
        return (_main_list, _sub_list)


    def _build_data_obj(self, *args) -> AbsSQLObj | None:
        
        _class_name = args[0]

        _return_class: AbsSQLObj = self._data_obj_dict.get(_class_name, None)
        if _return_class is None:
            return None
        
        _build_types = _return_class.get_types()
        args = self._enroll_args(_build_types, *args)
        _class_args = args[1:]
        
        _len_recieved = len(_class_args)
        _len_required = len(_build_types)
        
        if _len_required != _len_recieved:
            return None

        _return_obj = _return_class(*_class_args)
        return _return_obj