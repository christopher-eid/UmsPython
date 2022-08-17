from dependency_injector import containers, providers
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'course'))
import course_service


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # Gateways
    # database_client = providers.Singleton(
    #     sqlite3.connect,
    #     config.database.dsn,
    # )
    # Services
    course_service = providers.Factory(
        course_service.CourseService
    )
