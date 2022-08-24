from src.application.course.abstract_course_service import AbstractCourseService
from src.application.models.response_models.response_course_model import ResponseCourseModel
from src.application.exceptions.already_available_exception import AlreadyAvailableException
from src.application.models.response_models.status_model import StatusModel
'''
interface understanding from: https://realpython.com/python-interface/#formal-interfaces
interface abstraction understood from: https://www.askpython.com/python/oops/abstraction-in-python
'''


class CourseService(AbstractCourseService):

    def __init__(self, db, mongo_db):
        self.db = db
        self.mongo_db = mongo_db

    def add_course(self, received_course):
        #try:
        available_course = self.db.get_course(received_course.name)
        if available_course:
            raise AlreadyAvailableException("Course already existing")
        res = self.db.add_course(received_course)
        mx = res.max_students_number
        response = ResponseCourseModel(id=res.id, name=res.name, max_students_number=mx)
        return response
        # except AlreadyAvailableException:
        #     return StatusModel(success=False, description="Course Already Available")

    def add_course_to_mongo(self, received_course):
        try:
            available_course = self.mongo_db.get_course(received_course.name)
            if available_course:
                raise AlreadyAvailableException()
            res = self.mongo_db.add_course(received_course)
            mx = res["max_students_number"]
            response = ResponseCourseModel(id=res["id"], name=res["name"], max_students_number=mx)
            return response
        except AlreadyAvailableException:
            return StatusModel(success=False, description="Course Already Available")


