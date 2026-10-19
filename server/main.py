from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

@app.post('/signup')
def signup_user(user: UserCreate):
    # extract data coming from db
    print(user.name)
    print(user.email)
    print(user.password)
    # check user already exist
    # create new user and save in db
    pass  