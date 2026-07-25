from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()


class User(BaseModel):
    username: str
    lastname: str


@app.post("/generate-username")
def generate_username(user: User):
    generated_username = (
        user.username.lower()
        + user.lastname.lower()
        + str(random.randint(10, 99))
    )

    return {
        "username": user.username,
        "lastname": user.lastname,
        "generated_username": generated_username
    }