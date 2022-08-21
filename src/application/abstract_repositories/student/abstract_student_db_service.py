from abc import ABCMeta, ABC, abstractmethod


class AbstractStudentDBService(ABC):
    __metaclass__ = "ABCMeta"

    @abstractmethod
    def add_student(self, received_name:str, received_email:str):
        raise NotImplementedError

    @abstractmethod
    def get_student(self, received_name: str, received_email:str) -> list:
        raise NotImplementedError
