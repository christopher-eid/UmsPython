from abc import abstractmethod, ABC


class AbstractAddStudentsExcelService(ABC):
    __metaclass__ = "ABCMeta"

    @abstractmethod
    def add_students(self, received_excel):
        raise NotImplementedError



