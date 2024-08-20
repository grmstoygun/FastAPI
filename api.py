from fastapi import FastAPI
from pydantic import BaseModel

class CommandRequest(BaseModel):
    command : str

app = FastAPI()



@app.get("/")
async def root():
    return {"Hello World"}

@app.post("/command")
async def create_command(command:CommandRequest):
    return f"The command is {command.command}"

