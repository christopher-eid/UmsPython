from fastapi import FastAPI

from src.presentation.ums_web_api.routers import courses, students

'''
Setting up and starting up the app:
pip install fastapi
pip install "uvicorn[standard]"
uvicorn src.main:app --reload     <- use this command to run the server,it should reload automatically (because we added --reload).
http://127.0.0.1:8000/docs    for swagger
'''


app = FastAPI()

app.include_router(courses.router)
app.include_router(students.router)


#
# @app.post("/add_course")
# def read_root(received_course: CourseDTO):
#     return service1.add_course(received_course)



