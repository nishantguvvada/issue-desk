from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from model import invoke_model
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

origins = [
    f"{os.getenv('FRONTEND_URL')}"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def default():
    return { "status":"on" }

class UserInput(BaseModel):
    user_query: str

@app.post("/ask")
async def ask(user_input: UserInput):
    return { "response": await invoke_model(user_query=user_input.user_query) }

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=3000)