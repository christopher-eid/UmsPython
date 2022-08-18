import os
import sys

from dependency_injector import containers, providers

from src.application.course.course_service import CourseService
from src.application.course.course_interface import CourseInterface
from src.persistence.course.repositories import CourseDBService
from src.persistence.course.course_db_interface import CourseDBInterface
from src.persistence.connections.db_engine import DBEngine

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # Gateways
    # database_client = providers.Singleton(
    #     sqlite3.connect,
    #     config.database.dsn,
    # )
    # Services
    config = providers.Configuration()
    # services.UserInterface.register(services.UserService)
    # Gateways
    # database_client = providers.Singleton(
    #     sqlite3.connect,
    #     config.database.dsn,
    # )
    # Services

    db_engine = providers.Singleton(
        DBEngine
    )

    db_service = providers.Factory(
        CourseDBInterface.register(CourseDBService),
        engine=db_engine
    )

    course_service = providers.Factory(
        CourseInterface.register(CourseService),
        db=db_service
    )
