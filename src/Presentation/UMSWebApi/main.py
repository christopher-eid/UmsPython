from pydantic import BaseModel
from fastapi import FastAPI, Depends
from dependency_injector.wiring import Provide, inject
from dependency_injector import containers, providers
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'core', 'umsapplication', 'containers'))
import container
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'core', 'umsapplication', 'course'))
import course_service

'''
Note that this project is a just to test out the newly learned libraries
'''

'''
wise words from the pydantic docs:
pydantic is primarily a parsing library, not a validation library. Validation is a means to an end: building a model which conforms to the types and constraints provided.
In other words, pydantic guarantees the types and constraints of the output model, not the input data.
This might sound like an esoteric distinction, but it is not. If you're unsure what this means or how it might affect your usage you should read the section about Data Conversion below.
Although validation is not the src purpose of pydantic, you can use this library for custom validation.
'''

'''
Setting up and starting up the app:
pip install fastapi
pip install "uvicorn[standard]"
uvicorn src:app --reload     <- use this command to run the server,it should reload automatically (because we added --reload).
http://127.0.0.1:8000/docs    for swagger
'''

# dependancy injection related class:
# inspired from : https://github.com/ets-labs/python-dependency-injector/tree/master/examples/miniapps/application-single-container/example
# container = containers.Container()
# container.init_resources()
# container.wire(modules=[__name__])
# service1 = Provide[container.user_service]

service1 = ""

@inject
def main(service: course_service.CourseService = Provide[container.Container.course_service]) -> None:
    global service1
    service1 = service


if __name__ == "main":
    container = container.Container()
    container.init_resources()
    container.wire(modules=[__name__])
    main()


app = FastAPI()

class Item(BaseModel):
    item_id: int
    name: str
    price = 0.0


class Status(BaseModel):
    success = True
    description = "Operation Succeeded"


item1 = Item(item_id='1', name='potato', price='5.4')
item2 = Item(item_id='2', name='tomato', price='3.4')
items = [item1, item2]



@app.get("/")
def read_root():
    return service1.display_message("DEPENDENCY INJECTION DONE")


@app.get("/items/{item_id}")
def read_item(received_item_id: int):
    for i in items:
        if i.item_id == received_item_id:
            return i
    return Status(success=False, description="Item not found")


# if someone tries to send a json with a missing attribute, we will have an error
# EXCEPT for the price since we gave it a default value


@app.post("/items/{item_id}")
def add_item(item: Item):
    for i in items:
        if i.item_id == item.item_id:
            return Status(success=False, description="Id already available")
    items.append(item)
    return {"item_id": item.item_id, "item_name": item.name, "added": "Success"}
