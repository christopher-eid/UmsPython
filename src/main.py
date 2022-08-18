from fastapi import FastAPI

from src.presentation.ums_web_api.routers import courses

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



#
# @app.post("/add_course")
# def read_root(received_course: CourseDTO):
#     return service1.add_course(received_course)



