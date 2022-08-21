from abc import abstractmethod, ABC


class AbstractGetStudentsExcelService(ABC):
    __metaclass__ = "ABCMeta"

    @abstractmethod
    def get_students(self):
        raise NotImplementedError



