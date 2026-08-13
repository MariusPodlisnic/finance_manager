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

