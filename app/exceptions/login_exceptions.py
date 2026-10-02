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
class NotAuthenticated(AppException):
    def __init__(
            self):
        super().__init__(
            message="Not Authenticated",
            status_code=status.HTTP_403_FORBIDDEN,
            error_code="not_authenticated"
        )

class WrongCurrentPassword(AppException):
    def __init__(
            self):
        super().__init__(
            message="Wrong current password",
            status_code=status.HTTP_403_FORBIDDEN,
            error_code="wrong_current_password"
        )