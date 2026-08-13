from __future__ import annotations

from datetime import datetime
from uuid import UUID
from decimal import Decimal
from pydantic import BaseModel,ConfigDict,Field

class TransactionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:UUID
    amount:Decimal
    description:str | None
    category_id:UUID
    account_id:UUID
    created_at:datetime

class TransactionCreate(BaseModel):
    amount:Decimal = Field(gt=0,decimal_places=2)
    description:str | None = Field(
        default=None,
        max_length=255
    )
    category_id:UUID
    account_id:UUID
