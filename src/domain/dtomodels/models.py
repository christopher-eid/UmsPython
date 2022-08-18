from pydantic import BaseModel


class CourseModel(BaseModel):
    name: str
    max_students_number: int


class ReturnCourseModel(BaseModel):
    id: int
    name: str
    max_students_number: int


class StatusModel(BaseModel):
    success = True
    description = "Operation Succeeded"

