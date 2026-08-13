from uuid import UUID
from app.repositories.user_repository.base import UserRepository
from app.db.models import User
from app.api.schemas.user_schemas import UserCreate,UserUpdate
from app.exceptions.user_exceptions import UserEmailAlreadyExists,UserNotFoundError

class UserService:
    def __init__(self,repository:UserRepository):
        self.repository = repository

    def get_users(self):
        return self.repository.get_users()

    def create_user(self , request:UserCreate):
        email = request.email
        if email:
            existing_user = self.repository.get_by_email(email)
            if existing_user:
                raise UserEmailAlreadyExists(request.email)

        user = User(
            email=request.email,
            password=request.password
        )
        return self.repository.create(user)

    def get_user_by_id(self,user_id:UUID):
        user = self.repository.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError()
        return user

    def patch_user(self,user_id:UUID,request:UserUpdate):
        user = self.get_user_by_id(user_id)

        if request.email is not None:

            existing_user = self.repository.get_by_email(request.email)

            if existing_user and existing_user.id != user_id:
                raise UserEmailAlreadyExists(request.email)

        return self.repository.update(user, request)

    def delete_user(self,user_id:UUID) -> None:
        user = self.get_user_by_id(user_id)
        self.repository.delete_user(user)

