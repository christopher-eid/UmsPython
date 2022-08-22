from fastapi import APIRouter, UploadFile
from src.containers.container import Container
from fastapi.responses import FileResponse
import os
import shutil
from pathlib import Path

from starlette.background import BackgroundTasks
router = APIRouter()

# db_service = Container.db_service()
# db_in_excel = Container.db_in_excel()
# add_students_excel_handler_registration = Container.add_students_excel_handler_registration()

add_students_excel_service = Container.add_students_excel_service()
get_students_excel_service = Container.get_students_excel_service()


@router.post("/students/add_students_excel", tags=["Student"])
async def add_students_excel(received_excel: UploadFile):
    result = add_students_excel_service.add_students(received_excel)

    return result



@router.get("/students/get_students_excel", tags=["Student"])
async def get_students_excel():
    result = get_students_excel_service.get_students()
    return result


@router.post("/students/add_students_excel_mediatr", tags=["Student"])
async def add_students_excel_mediatr(received_excel: int):
    return "hi"
    # request = AddStudentsExcelCommand(received_excel)
    # result = add_students_excel_handler_registration.send(request)

    # mediator = Mediator()
    # request = AddStudentsExcelCommand(received_excel)
    # result = mediator.send(request)
   # result = await mediator.send_async(request)  #in async mode