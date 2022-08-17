import abc
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'infrastructure', 'umspersistence', 'course'))
import course_db_service
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'umsdomain', 'dtomodels'))
import models

class CourseInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'add_course') and
                callable(subclass.add_course) or
                NotImplemented)

    #@abc.abstractmethod
    def add_course(self, received_course):
        res = course_db_service.CourseDBService.add_course(received_course)
        if res:
            mx = res.max_students_number
            response = models.ReturnCourseDTO(id=res.id, name=res.name, max_students_number=mx)
        return response
        #raise NotImplementedError


#now we can add all services related to course inside this abstract class and we are able to directly use them
#from our service