from abc import abstractmethod, ABC


class AbstractCourseService(ABC):
    __metaclass__ = "ABCMeta"

    @abstractmethod
    def add_course(self, received_course):
        raise NotImplementedError

    @abstractmethod
    def add_course_to_mongo(self, received_course):
        raise NotImplementedError

