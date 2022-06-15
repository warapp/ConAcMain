import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from action import Action

app = FastAPI()


class User(BaseModel):
    username: Optional[str]
    password: Optional[str]
    

# -----------rout--------------
@app.get("/")
async def read_root():
    return {"hello": "world"}


@app.get("/hw/get")
async def hw_get():
    data = Action.getHW()
    return data


@app.get("/hw/get_by_id")
async def hw_get_by_id(ID):
    data = Action.getHWByID(ID)
    return data


@app.get("/hw/get_by_name")
async def hw_get_by_name(name):
    data = Action.getHWByName(name)
    return data


@app.get("/hw/add_hw")
async def hw_add_hw(name, hw_name):
    data = Action.addHW(name, hw_name)

@app.get("hello")
async def hello():
    data = "สวัสดีค้าบ"
    return data

@app.get("/my_name")
async def my_name():
    data = "wara phon"
    return data

@app.get("/hw/update_value_hw")
async def hw_update_status_hw(ID, value):
    data = Action.updateValueHW(ID, value)
    return data


@app.get("/hw/delete_hw")
async def hw_update_status_hw(ID):
    data = Action.DeleteHW(ID)
    return data


@app.post("/register")
async def registers(user: User):
    data = Action.register(user)
    return data

@app.get("/update_status_hw")
async def updateStatushw(ID,status):
    data = Action.update_status_hw(ID,status)
    return data

@app.get("/add_hw_name")
async def insertHW(name,hw_name):
    data = Action.insertHW(name,hw_name)
    return data
    
    

if __name__ == "__main__":
    uvicorn.run(app,host="192.168.90.210", port=8000)