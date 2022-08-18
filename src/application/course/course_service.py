from src.application.course.abstract_course_service import AbstractCourseService
from src.domain.dtomodels.return_course_model import ReturnCourseModel
from src.application.exceptions.already_available_exception import AlreadyAvailableException
from src.domain.dtomodels.status_model import StatusModel
'''
interface understanding from: https://realpython.com/python-interface/#formal-interfaces
interface abstraction understood from: https://www.askpython.com/python/oops/abstraction-in-python
'''


class CourseService(AbstractCourseService):

    def __init__(self, db):
        self.db = db

    def add_course(self, received_course):
        try:
            available_course = self.db.get_course(received_course.name)
            if available_course:
                raise AlreadyAvailableException()
            res = self.db.add_course(received_course)
            mx = res.max_students_number
            response = ReturnCourseModel(id=res.id, name=res.name, max_students_number=mx)
            return response
        except AlreadyAvailableException:
            return StatusModel(success=False, description="Course Already Available")


