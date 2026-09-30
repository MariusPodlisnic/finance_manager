
from starlette import status
from app.utils.custom_exception import AppException

class AccountNotFoundError(AppException):
    def __init__(
        self,
        account_id: int
    ):
        super().__init__(
            message=f"Account with id {account_id} was not found",
            status_code=status.HTTP_404_NOT_FOUND,
            error_code="account_not_found"
        )

class AccountAlreadyExists(AppException):
    def __init__(
        self,
        name:str
    ):
        super().__init__(
            message=f"Account with name {name} already exists",
            status_code=status.HTTP_403_FORBIDDEN,
            error_code="account_already_exists"
        )

class InvalidCurrency(AppException):
    def __init__(
        self,
        currency:str
    ):
        super().__init__(
            message=f"Currency {currency} not supported",
            status_code=status.HTTP_403_FORBIDDEN,
            error_code="invalid_currency"
        )