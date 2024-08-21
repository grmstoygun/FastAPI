from fastapi import FastAPI
from pydantic import BaseModel
import myNetmiko

class CommandRequest(BaseModel):
    command : str

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello World"}

@app.post("/command")
async def create_command(command:CommandRequest):
    netmiko_response =  await myNetmiko.sendCommand(command.command)
    return netmiko_response 

