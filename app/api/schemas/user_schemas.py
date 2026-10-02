from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel,ConfigDict,EmailStr

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:int
    created_at:datetime

class UserCreate(BaseModel):
    email:EmailStr
    password:str
    role:str

class UserUpdate(BaseModel):
    email:EmailStr

class UserChangePassword(BaseModel):
    current_password:str
    new_password:str