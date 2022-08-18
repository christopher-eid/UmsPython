from src.application.course.course_interface import CourseInterface
from src.domain.dtomodels.models import ReturnCourseModel
#IN OUR CASE HERE, WHEN WE CREATE AN INSTANCE OF UserService, we can use the method display_message even if we did not
#write it inside the service, since it is defined inside the interface. so this is how we did abstraction


#interface understanding from: https://realpython.com/python-interface/#formal-interfaces
#interface abstraction understood from: https://www.askpython.com/python/oops/abstraction-in-python


class CourseService(CourseInterface):

    def __init__(self, db):
        self.db = db

    def add_course(self, received_course):
        res = self.db.add_course(received_course)
        mx = res.max_students_number
        response = ReturnCourseModel(id=res.id, name=res.name, max_students_number=mx)
        return response

