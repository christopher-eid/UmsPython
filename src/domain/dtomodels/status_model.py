from pydantic import BaseModel


class StatusModel(BaseModel):
    success = True
    description = "Operation Succeeded"
