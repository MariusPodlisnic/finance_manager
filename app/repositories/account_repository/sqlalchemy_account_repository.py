from __future__ import annotations
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.api.schemas.account_schemas import AccountUpdate
from app.db.models import Account
from app.repositories.account_repository.base import AccountRepository

class SqlAlchemyAccountRepository(AccountRepository):
    def __init__(self,db:Session):
        self.db = db

    def get_accounts(
            self,
            user_id:int) -> list[Account]:
        statement = select(Account).where(Account.user_id == user_id)
        return list(self.db.scalars(statement))
    def get_by_name(self,
                    name:str,
                    user_id: int) -> Account | None:
        statement = select(Account).where(
            Account.name == name,
                        Account.user_id == user_id
        )
        account = self.db.scalar(statement)
        return account
    def get_by_id(self,
                  account_id:int,
                  user_id:int) -> Account | None:
        statement = select(Account).where(
            Account.id == account_id,
            Account.user_id == user_id
        )
        account = self.db.scalar(statement)
        return account
    def create_account(self,
                       data:Account) -> Account:
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)

        return data

    def update(self,
               account:Account,
               data:AccountUpdate) -> Account:
        updated_data = data.model_dump(exclude_unset=True)
        for field,value in updated_data.items():
            setattr(account,field,value)

        self.db.commit()
        self.db.refresh(account)

        return account

    def delete_account(self,
               account:Account) ->None:
        self.db.delete(account)
        self.db.commit()

