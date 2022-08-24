from fastapi import APIRouter, HTTPException

from src.application.exceptions.application_based_exception import ApplicationBasedException
from src.containers.container import Container
from src.application.models.request_models.course_model import CourseModel

router = APIRouter()
course_service = Container.course_service()



@router.post("/courses/add_course")
async def add_course(received_course: CourseModel):
    try:
        return course_service.add_course(received_course)
    except ApplicationBasedException as e1:
        raise HTTPException(status_code=400, detail=e1.message)
    except Exception as e2:
        raise HTTPException(status_code=500, detail=e2.__cause__)


@router.post("/courses/add_course_to_mongo")
async def add_course_to_mongo(received_course: CourseModel):
    return course_service.add_course_to_mongo(received_course)



