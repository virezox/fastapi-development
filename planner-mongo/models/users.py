from typing import List, Optional

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@github.com",
                "password": "strong!!!",
            }
        }

    class Settings:
        name = "users"


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@github.com",
                "password": "strong!!!",
            }
        }
