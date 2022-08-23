from fastapi import APIRouter, UploadFile, Depends
from src.containers.container import Container
from starlette.responses import JSONResponse


router = APIRouter()

# db_service = Container.db_service()
# db_in_excel = Container.db_in_excel()
# add_students_excel_handler_registration = Container.add_students_excel_handler_registration()

add_students_excel_service = Container.add_students_excel_service()
get_students_excel_service = Container.get_students_excel_service()
authentication_service = Container.firebase_auth_service()

@router.post("/students/add_students_excel")
async def add_students_excel(received_excel: UploadFile,  jwt_verify=Depends(authentication_service.verify_access_token)):
    if type(jwt_verify) == JSONResponse:
        return jwt_verify
    result = add_students_excel_service.add_students(received_excel)

    return result



@router.get("/students/get_students_excel")
async def get_students_excel(jwt_verify=Depends(authentication_service.verify_access_token)):
    if type(jwt_verify) == JSONResponse:
        return jwt_verify
    result = get_students_excel_service.get_students()
    return result


@router.post("/students/add_students_excel_mediatr")
async def add_students_excel_mediatr(received_excel: int):
    return "coming soon, check comments in endpoint"
    # request = AddStudentsExcelCommand(received_excel)
    # result = add_students_excel_handler_registration.send(request)

    # mediator = Mediator()
    # request = AddStudentsExcelCommand(received_excel)
    # result = mediator.send(request)
   # result = await mediator.send_async(request)  #in async mode
