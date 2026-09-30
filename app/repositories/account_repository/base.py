from __future__ import annotations

from uuid import UUID
from typing import Protocol

from app.api.schemas.account_schemas import AccountUpdate, AccountCreate
from app.db.models import Account
class AccountRepository(Protocol):
    def get_accounts(
            self,
            user_id:int) -> list[Account]:...
    def get_by_name(self,
                    name:str,
                    user_id: int) ->Account | None:...
    def get_by_id(self,
                  account_id:int,
                  user_id:int) -> Account | None:...
    def create_account(self,
                       data:Account) -> Account:...
    def update(self,
               account:Account,
               data:AccountUpdate) -> Account:...
    def delete_account(self,
               account:Account) -> None:...


