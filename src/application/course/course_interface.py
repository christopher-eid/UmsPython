from abc import abstractmethod, ABC


class CourseInterface(ABC):
    __metaclass__ = "ABCMeta"
    @abstractmethod
    def add_course(self, received_course):

        raise NotImplementedError

