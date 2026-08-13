from __future__ import annotations

from uuid import UUID
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel,ConfigDict,Field
from app.utils.enums.currency_type import CurrencyType

class AccountResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:UUID
    name:str
    balance:Decimal
    currency:CurrencyType
    created_at:datetime

class AccountCreate(BaseModel):
    name:str = Field(min_length=1,max_length=255)
    currency:CurrencyType

class AccountUpdate(BaseModel):
    name:str | None = Field(
        default=None,
        min_length=1,
        max_length=255
    )
    currency:CurrencyType | None = None