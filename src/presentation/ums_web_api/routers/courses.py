from fastapi import APIRouter
from dependency_injector.wiring import inject
from src.application.containers.container import Container
from src.domain.dtomodels.models import CourseModel
from dependency_injector.wiring import Provide, inject
router = APIRouter()

@inject
def main() -> None:
    pass


if __name__ == "src.presentation.ums_web_api.routers.courses":
    # reg2 = Container.db_connection()
    # reg1 = Container.db_service()
    reg = Container.course_service()
    main()


@router.post("/courses/add_course", tags=["Add Course"])
async def read_users(received_course: CourseModel):
    return reg.add_course(received_course)

