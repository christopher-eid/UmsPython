
from fastapi import FastAPI, Header, Request
from fastapi.responses import JSONResponse
from src.presentation.ums_web_api.routers import courses, authentication
from src.containers.container import Container
from firebase_admin import _auth_utils



#for middleware with logger to display time for each request
#pip install python-time to be able to import time , PYTHON-TIME NOT TIME

import time
import logging
logging.basicConfig(format='[%(asctime)s %(levelname)s]:%(message)s', level=logging.INFO)
#to disable uvicorn standard loggers
uvicorn_error = logging.getLogger("uvicorn.error")
uvicorn_error.disabled = True
uvicorn_access = logging.getLogger("uvicorn.access")
uvicorn_access.disabled = True


'''
Setting up and starting up the app:
pip install fastapi
pip install "uvicorn[standard]"
uvicorn main:app --reload     <- use this command to run the server,it should reload automatically (because we added --reload).
http://127.0.0.1:8000/docs    for swagger
'''


app = FastAPI()

app.include_router(courses.router)
app.include_router(authentication.router)
serv = Container.firebase_auth_service()


#raise JSON response of code 401 to indicate that there is an error in jwt token received
#do not forget to check first if jwt token is in header list or else we will have error
#jwt_token in python arguments becomes jwt-token in header fields (- instead of _)


@app.middleware("http") #HTTP NOT HTTPS!!!!!!!!
async def check_jwt_token_header(request: Request, call_next):

    if "jwt-token" in request.headers:
        token = request.headers["jwt-token"] #PUT jwt-token NOT jwt_token because in headers _ becomes -
        try:
            firebase_user_id = serv.verify_access_token(token)

        except _auth_utils.InvalidIdTokenError:
            return JSONResponse(status_code=401, content={'reason': 'invalid jwt token'})

    response = await call_next(request)
    return response

@app.middleware("http")
async def log_process_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logging.info(" endpoint url:" + str(request.url) + " - process time: " + str(process_time) + "seconds")
    return response




