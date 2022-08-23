from abc import ABCMeta, ABC, abstractmethod


class AbstractCourseNoSqlRepository(ABC):
    __metaclass__ = "ABCMeta"

    @abstractmethod
    def add_course(self, received_course):
        raise NotImplementedError

    @abstractmethod
    def get_course(self, received_name: str) -> list:
        raise NotImplementedError
