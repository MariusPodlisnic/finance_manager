from starlette import status

from app.utils.custom_exception import AppException

class WrongCredentials(AppException):
    def __init__(
            self):
        super().__init__(
            message="Could not validate credentials",
            status_code=status.HTTP_403_FORBIDDEN,
            error_code="wrong_credentials"
        )