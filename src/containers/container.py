from dependency_injector import containers, providers

from src.application.course.course_service import CourseService
from src.application.course.abstract_course_service import AbstractCourseService
from src.persistence.repositories.course.course_db_service import CourseDBService
from src.application.abstract_repositories.course.abstract_course_db_service import AbstractCourseDBService
from src.persistence.connections.db_engine import DBEngine
from src.persistence.mongo_repositories.course.course_mongo_service import CourseMongoService
from src.application.abstract_mongo_repositories.course.abstract_course_mongo_service import AbstractCourseMongoService
from src.persistence.connections.mongo_db_client import MongoDBClient

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

    db_service = providers.Factory(
        AbstractCourseDBService.register(CourseDBService),
        engine=db_engine
    )

    mongo_db_service = providers.Factory(
        AbstractCourseMongoService.register(CourseMongoService),
        mongo_db_client = mongo_db_client
    )

    course_service = providers.Factory(
        AbstractCourseService.register(CourseService),
        db=db_service,
        mongo_db = mongo_db_service
    )

    #firebase
    firebase_engine = providers.Singleton(
        FirebaseEngine
    )

    firebase_auth_service = providers.Singleton(
        AbstractFirebaseAuthService.register(FirebaseAuthService),
        firebase_engine=firebase_engine
    )
