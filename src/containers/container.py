from dependency_injector import containers, providers

from src.application.course.course_service import CourseService
from src.application.course.abstract_course_service import AbstractCourseService
from src.persistence.repositories.course.course_db_service import CourseDBService
from src.application.abstract_repositories.course.abstract_course_db_service import AbstractCourseDBService
from src.persistence.connections.db_engine import DBEngine
from src.persistence.mongo_repositories.course.course_mongo_service import CourseMongoService
from src.application.abstract_mongo_repositories.course.abstract_course_mongo_service import AbstractCourseMongoService
from src.persistence.connections.mongo_db_client import MongoDBClient

from src.application.student_cqrs.commands.add_students_excel.add_students_excel_service import AddStudentsExcelService
from src.application.student_cqrs.commands.add_students_excel.abstract_add_students_excel_service import AbstractAddStudentsExcelService
from src.application.abstract_repositories.student.abstract_student_db_service import AbstractStudentDBService
from src.persistence.repositories.student.student_db_service import StudentDBService

from src.application.student_cqrs.queries.get_students_excel.get_students_excel_service import GetStudentsExcelService
from src.application.student_cqrs.queries.get_students_excel.abstract_get_students_excel_service import AbstractGetStudentsExcelService


from src.application.student_cqrs.commands.add_students_excel_mediatr.add_students_excel_command import AddStudentsExcelCommand
from src.application.student_cqrs.commands.add_students_excel_mediatr.add_students_excel_command_handler import AddStudentsExcelCommandHandler


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_engine = providers.Singleton(
        DBEngine
    )

    mongo_db_client = providers.Singleton(
        MongoDBClient
    )

    db_course_service = providers.Factory(
        AbstractCourseDBService.register(CourseDBService),
        engine=db_engine
    )

    mongo_db_service = providers.Factory(
        AbstractCourseMongoService.register(CourseMongoService),
        mongo_db_client = mongo_db_client
    )

    course_service = providers.Factory(
        AbstractCourseService.register(CourseService),
        db=db_course_service,
        mongo_db=mongo_db_service
    )

    db_student_service = providers.Factory(
        AbstractStudentDBService.register(StudentDBService),
        engine=db_engine
    )

    add_students_excel_service = providers.Factory(
        AbstractAddStudentsExcelService.register(AddStudentsExcelService),
        db=db_student_service
    )

    get_students_excel_service = providers.Factory(
        AbstractGetStudentsExcelService.register(GetStudentsExcelService),
        db=db_student_service
    )
    # mediator = providers.Factory(
    #     Mediator
    # )
    #
    # db_in_excel = providers.Factory(
    #     AddStudentsExcelCommandHandler,
    #     db_service=db_service
    # )

    #register handler in mediator
    # add_students_excel_handler_registration = providers.Singleton(
    #     AddStudentsExcelCommand.register(AddStudentsExcelCommandHandler),
    #     db_service = db_service
    # )
