from fastapi import APIRouter, Header
from src.containers.container import Container
from src.domain.dtomodels.course_model import CourseModel
from typing import Union

router = APIRouter()
reg = Container.course_service()

# @inject
# def main() -> None:
#     pass
#
#
# if __name__ == "src.presentation.ums_web_api.routers.courses":
#     # reg2 = Container.db_connection()
#     # reg1 = Container.db_service()
#     main()


@router.post("/courses/add_course", tags=["Add Course"])
async def add_course(received_course: CourseModel, jwt_token: Union[str, None] = Header(default=None)):
    return reg.add_course(received_course)


@router.post("/courses/add_course_to_mongo", tags=["Add Course"])
async def add_course_to_mongo(received_course: CourseModel, jwt_token: Union[str, None] = Header(default=None)):
    return reg.add_course_to_mongo(received_course)

