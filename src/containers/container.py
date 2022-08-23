from dependency_injector import containers, providers

from src.application.course.course_service import CourseService
from src.application.course.abstract_course_service import AbstractCourseService
from src.persistence.sql_repositories.course.course_sql_repository import CourseSqlRepository
from src.domain.abstract_sql_repositories.course.abstract_course_sql_repository import AbstractCourseSqlRepository
from src.persistence.connections.db_engine import DBEngine
from src.persistence.nosql_repositories.course.course_nosql_repository import CourseNoSqlRepository
from src.domain.abstract_nosql_repositories.course.abstract_course_nosql_repository import AbstractCourseNoSqlRepository
from src.persistence.connections.mongo_db_client import MongoDBClient


from src.application.student_cqrs.commands.add_students_excel.add_students_excel_service import AddStudentsExcelService
from src.application.student_cqrs.commands.add_students_excel.abstract_add_students_excel_service import AbstractAddStudentsExcelService
from src.domain.abstract_sql_repositories.student.abstract_student_sql_repository import AbstractStudentSqlRepository
from src.persistence.sql_repositories.student.student_sql_repository import StudentSqlRepository

from src.application.student_cqrs.queries.get_students_excel.get_students_excel_service import GetStudentsExcelService
from src.application.student_cqrs.queries.get_students_excel.abstract_get_students_excel_service import AbstractGetStudentsExcelService

#firebase:
from src.infrastructure.ums_infrastucture.firebase_connection.firebase_engine import FirebaseEngine
from src.infrastructure.ums_infrastucture.firebase_jwt_token.firebase_auth_service import FirebaseAuthService
from src.infrastructure.ums_infrastructure_abstraction.firebase_jwt_token.abstract_firebase_auth_service \
    import AbstractFirebaseAuthService



class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_engine = providers.Singleton(
        DBEngine
    )

    mongo_db_client = providers.Singleton(
        MongoDBClient
    )

    db_course_service = providers.Factory(
        AbstractCourseSqlRepository.register(CourseSqlRepository),
        engine=db_engine
    )

    mongo_db_service = providers.Factory(
        AbstractCourseNoSqlRepository.register(CourseNoSqlRepository),
        mongo_db_client = mongo_db_client
    )

    course_service = providers.Factory(
        AbstractCourseService.register(CourseService),
        db=db_course_service,
        mongo_db=mongo_db_service
    )

    db_student_service = providers.Factory(
        AbstractStudentSqlRepository.register(StudentSqlRepository),
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

    #firebase
    firebase_engine = providers.Singleton(
        FirebaseEngine
    )

    firebase_auth_service = providers.Factory(
        AbstractFirebaseAuthService.register(FirebaseAuthService),
        firebase_engine=firebase_engine
    )
