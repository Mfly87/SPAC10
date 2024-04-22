from .abs_data_obj import AbsDataObj
import abc

class AbsSQLObj(AbsDataObj):

    @abc.abstractstaticmethod
    def get_headers() -> list[str]:
        pass

    @abc.abstractstaticmethod
    def get_types() -> list[type]:
        pass

    @abc.abstractmethod
    def get_values() -> list[type]:
        pass

    @staticmethod    
    def get_build_headers(_class_type: 'AbsSQLObj') -> list[any]:
        '''
        Returns a list of headers required to reconstruct the object\n
        Used for automatically constructing SQL tables
        '''

        _list_of_headers: list = ["class"]
        for _value, _type in zip(_class_type.get_headers(), _class_type.get_types()):
            if issubclass(_type, AbsSQLObj):
                _list_of_headers += AbsSQLObj.get_build_headers(_type)[1:]
            else:
                _list_of_headers.append(_value)
        return _list_of_headers

    @staticmethod
    def get_build_types(_class_type: 'AbsSQLObj') -> list[any]:
        '''
        Returns a list of types required to reconstruct the object\n
        Used for automatically constructing SQL tables
        '''

        _list_of_headers: list = [str]
        for _type in _class_type.get_types():
            if issubclass(_type, AbsSQLObj):
                _list_of_headers += AbsSQLObj.get_build_types(_type)[1:]
            else:
                _list_of_headers.append(_type)
        return _list_of_headers
    
    def get_build_values(self) -> list[any]:
        '''
        Returns a list of values required to reconstruct the object\n
        Used for automatically constructing SQL tables
        '''

        _list_of_values: list = [self.__class__.__name__]
        for _value, _type in zip(self.get_values(), self.get_types()):
            if issubclass(_type, AbsSQLObj):
                _list_of_values += _value.get_build_values()[1:]
            else:
                _list_of_values.append(_value)
        return _list_of_values
