import abc

class AbsDataObj(abc.ABC):

    @abc.abstractmethod
    def to_string(self):
        pass