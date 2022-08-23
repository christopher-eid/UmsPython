from fastapi import FastAPI, Request

from src.presentation.ums_web_api.routers import courses


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


#
# service1 = ""
# @inject
# def main(service: CourseService = Provide[Container.course_service]) -> None:
#     global service1
#     service1 = service
#
#
# if __name__ == "src.main":
#     container = Container()
#     container.init_resources()
#     container.wire(modules=[__name__])
#     main()


app = FastAPI()

app.include_router(courses.router)

@app.middleware("http")
async def log_process_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logging.info(" endpoint url:" + str(request.url) + " - process time: " + str(process_time) + "seconds")
    return response

#
# @app.post("/add_course")
# def read_root(received_course: CourseDTO):
#     return service1.add_course(received_course)



