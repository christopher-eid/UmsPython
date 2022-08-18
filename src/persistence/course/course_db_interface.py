from abc import ABCMeta, ABC, abstractmethod


class CourseDBInterface(ABC):
    __metaclass__ = "ABCMeta"

    @abstractmethod
    def add_course(self, received_course):
        raise NotImplementedError

