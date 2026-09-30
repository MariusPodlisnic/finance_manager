from __future__ import annotations
from pydantic import BaseModel,ConfigDict,Field
from app.utils.enums.transaction_type import TransactionType

class CategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:int
    name:str
    type:TransactionType

class CategoryCreate(BaseModel):
    name:str = Field(min_length=1,max_length=255)
    type:TransactionType

class CategoryUpdate(BaseModel):
    name:str | None = Field(
        default=None,
        min_length=1,
        max_length=255
    )
