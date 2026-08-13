from uuid import UUID
from starlette import status
from app.utils.custom_exception import AppException

class UserNotFoundError(AppException):
    def __init__(
        self,
        user_id: UUID
    ):
        super().__init__(
            message=f"User with id {user_id} was not found",
            status_code=status.HTTP_404_NOT_FOUND,
            error_code="owner_not_found"
        )

class UserEmailAlreadyExists(AppException):
    def __init__(
        self,
        email:str
    ):
        super().__init__(
            message=f"User with email {email} already exists",
            status_code=status.HTTP_409_CONFLICT,
            error_code="user_email_already_exists"
        )

