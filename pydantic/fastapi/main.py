from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str = "Robiz"
    admin_email: str = "admin@gmail.com"

def get_settings():
    return Settings()

@app.post("/signup")
def signup(user: UserSignup):
    return {'message': f'User {user.username} signed up successfully'}

@app.get('/settings')
def get_settings_endpoint(settings: Settings = Depends()):
    return settings