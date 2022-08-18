from dependency_injector import containers, providers

from src.application.course.course_service import CourseService
from src.application.course.abstract_course_service import AbstractCourseService
from src.persistence.repositories.course.course_db_service import CourseDBService
from src.application.abstract_repositories.course.abstract_course_db_service import AbstractCourseDBService
from src.persistence.connections.db_engine import DBEngine


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_engine = providers.Singleton(
        DBEngine
    )

    db_service = providers.Factory(
        AbstractCourseDBService.register(CourseDBService),
        engine=db_engine
    )

    course_service = providers.Factory(
        AbstractCourseService.register(CourseService),
        db=db_service
    )
