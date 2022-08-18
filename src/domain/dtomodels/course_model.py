from pydantic import BaseModel


class CourseModel(BaseModel):
    name: str
    max_students_number: int
