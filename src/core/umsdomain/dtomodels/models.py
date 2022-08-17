from pydantic import BaseModel


class CourseDTO(BaseModel):
    name: str
    max_students_number: int


class ReturnCourseDTO(BaseModel):
    id: int
    name: str
    max_students_number: int


class Status(BaseModel):
    success = True
    description = "Operation Succeeded"

