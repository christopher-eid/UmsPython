from fastapi import APIRouter, Header, Depends
from starlette.responses import JSONResponse

from src.containers.container import Container
from firebase_admin import _auth_utils

from typing import Union

router = APIRouter()

authentication_service = Container.firebase_auth_service()


#WE CAN DIRECTLY USE THE SERVICE TO VERIFY TOKEN FROM THE ENDPOINT USING Depends(service.functionName)
#we can see that the service parameters that we need in our service will automatically appear at the endpoint in swagger
#to learn about depends: https://fastapi.tiangolo.com/tutorial/dependencies/



@router.post("/firebase/sign_in")
async def sign_in(received_email: str, received_password:str):
    return authentication_service.sign_in_access_and_refresh_token(received_email, received_password)

@router.post("/firebase/refresh_token")
async def refresh_token(received_refresh_token: str):
    return authentication_service.refresh_token(received_refresh_token)


@router.post("/firebase/verify_access_token")
async def verify_access_token(received_access_token: str):
    try:
        return authentication_service.verify_access_token(received_access_token)
    except _auth_utils.InvalidIdTokenError:
        return JSONResponse(status_code=401, content={'reason': 'invalid jwt token'})


@router.post("/verify_token_dependency_injection_testing")
async def test_firebase_middleware(received_text: str,  jwt_verify=Depends(authentication_service.verify_access_token)):
    if type(jwt_verify) == JSONResponse:
        return jwt_verify

    return received_text

