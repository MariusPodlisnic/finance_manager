from __future__ import annotations

from uuid import UUID
from datetime import datetime
from pydantic import BaseModel,ConfigDict,EmailStr

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:UUID
    created_at:datetime

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserUpdate(BaseModel):
    email:EmailStr