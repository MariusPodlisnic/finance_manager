from __future__ import annotations

from uuid import UUID
from typing import Protocol

from app.api.schemas.account_schemas import AccountUpdate
from app.db.models import Account
class AccountRepository(Protocol):
    def get_accounts(
            self,
            user_id:UUID) -> list[Account]:...
    def get_by_id(self,
                  account_id:UUID,
                  user_id:UUID) -> Account | None:...
    def create_account(self,
                       data:Account) -> Account:...
    def update(self,
               account:Account,
               data:AccountUpdate) -> Account:...
    def delete_account(self,
               account:Account) -> None:...


