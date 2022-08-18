from pydantic import BaseModel


class ReturnCourseModel(BaseModel):
    id: int
    name: str
    max_students_number: int
