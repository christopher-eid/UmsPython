import abc


class CourseInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'display_message') and
                callable(subclass.display_message) or
                NotImplemented)

    #@abc.abstractmethod
    def display_message(self, message: str):
        return {"Message": message}
        #return UserService.display_message("hello")
        #raise NotImplementedError