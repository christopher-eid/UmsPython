from pydantic import BaseModel
from fastapi import FastAPI, Depends
from dependency_injector.wiring import Provide, inject
from dependency_injector import containers, providers
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'containers'))
# import containers
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'services'))
# import services



'''
Setting up and starting up the app:
pip install fastapi
pip install "uvicorn[standard]"
uvicorn main:app --reload     <- use this command to run the server,it should reload automatically (because we added --reload).
http://127.0.0.1:8000/docs    for swagger
'''


#
# service1 = ""
#
# @inject
# def main(service: services.UserService = Provide[containers.Container.user_service]) -> None:
#     global service1
#     service1 = service
#
#
# if __name__ == "main":
#     container = containers.Container()
#     container.init_resources()
#     container.wire(modules=[__name__])
#     main()
#

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
    return Status()
   # return service1.displaymessage("DEPENDENCY INJECTION DONE")


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
