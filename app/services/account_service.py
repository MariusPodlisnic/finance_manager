from app.db.models import Account
from app.api.schemas.account_schemas import AccountUpdate,AccountCreate
from app.repositories.account_repository.base import AccountRepository
from app.exceptions.account_exceptions import AccountNotFoundError,AccountAlreadyExists,InvalidCurrency
from app.utils.enums.currency_type import CurrencyType


class AccountService:
    def __init__(self,repository:AccountRepository):
        self.repository = repository

    def get_accounts(self,
                     user_id: int):
        return self.repository.get_accounts(user_id)

    def get_account_by_id(self,
                          user_id: int,
                          account_id: int):
        account = self.repository.get_by_id(user_id,account_id)
        if not account:
            raise AccountNotFoundError(account_id)
        return account
    def create_account(self,user_id: int, request:AccountCreate):
        name = request.name
        if name:
            existing_name = self.repository.get_by_name(name,user_id)
            if existing_name:
                raise AccountAlreadyExists(name)
        account = Account(
            name = request.name,
            balance=request.balance,
            currency = request.currency,
            user_id = user_id
        )
        return self.repository.create_account(account)

    def update_account(self,user_id: int, account_id: int,request: AccountUpdate):
        account = self.repository.get_by_id(account_id,user_id)
        currency = request.currency
        if request.name is not None:
            existing_account = self.repository.get_by_name(request.name,user_id)
            if existing_account and existing_account.id != user_id:
                raise AccountAlreadyExists(request.name)
        if currency and currency not in CurrencyType:
            raise InvalidCurrency(currency)
        return self.repository.update(account,request)

    def delete_account(self,user_id: int , account_id: int):
        account = self.get_account_by_id(account_id,user_id)
        self.repository.delete_account(account)