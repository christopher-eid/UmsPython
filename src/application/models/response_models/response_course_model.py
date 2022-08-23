from pydantic import BaseModel


class ResponseCourseModel(BaseModel):
    id: int
    name: str
    max_students_number: int
