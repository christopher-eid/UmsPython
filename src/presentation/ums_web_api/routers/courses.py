from fastapi import APIRouter
from src.containers.container import Container
from src.domain.dtomodels.course_model import CourseModel

router = APIRouter()
reg = Container.course_service()


@router.post("/courses/add_course", tags=["Course"])
async def add_course(received_course: CourseModel):
    return reg.add_course(received_course)


@router.post("/courses/add_course_to_mongo", tags=["Course"])
async def add_course_to_mongo(received_course: CourseModel):
    return reg.add_course_to_mongo(received_course)



