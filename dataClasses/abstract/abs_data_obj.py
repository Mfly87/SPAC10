import abc

class AbsDataObj(abc.ABC):

    @abc.abstractmethod
    def to_string(self):
        pass

    def __str__(self) -> str:
        return self.to_string()