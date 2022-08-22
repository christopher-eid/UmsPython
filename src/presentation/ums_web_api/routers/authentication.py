from fastapi import APIRouter, Header
from src.containers.container import Container
from firebase_admin import _auth_utils

from typing import Union

router = APIRouter()

authentication_service = Container.firebase_auth_service()


@router.post("/firebase_middleware_testing", tags=["Firebase"])
async def test_firebase_middleware(received_text: str, jwt_token: Union[str, None] = Header(default=None)):
    return received_text

@router.post("/firebase/sign_in", tags=["Firebase"])
async def sign_in(received_email: str, received_password:str):
    return authentication_service.sign_in_access_and_refresh_token(received_email, received_password)


@router.post("/firebase/verify_access_token", tags=["Firebase"])
async def verify_access_token(received_access_token: str):
    try:
        return authentication_service.verify_access_token(received_access_token)
    except _auth_utils.InvalidIdTokenError:
        return JSONResponse(status_code=401, content={'reason': 'invalid jwt token'})


@router.post("/firebase/refresh_token", tags=["Firebase"])
async def refresh_token(received_refresh_token: str):
    return authentication_service.refresh_token(received_refresh_token)