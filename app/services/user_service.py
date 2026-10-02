from app.repositories.user_repository.base import UserRepository
from app.db.models import User
from app.api.schemas.user_schemas import UserCreate,UserUpdate,UserChangePassword
from app.exceptions.user_exceptions import UserEmailAlreadyExists,UserNotFoundError
from app.exceptions.login_exceptions import WrongCurrentPassword
from app.utils.password import hash_password,verify_password

class UserService:
    def __init__(self,repository:UserRepository):
        self.repository = repository

    def get_users(self,):
        return self.repository.get_users()

    def create_user(self , request:UserCreate):
        email = request.email
        hashed_password = hash_password(request.password)
        if email:
            existing_user = self.repository.get_by_email(email)
            if existing_user:
                raise UserEmailAlreadyExists(request.email)

        user = User(
            email=request.email,
            password=hashed_password,
            role=request.role
        )
        return self.repository.create(user)

    def get_user_by_id(self,user_id:int):
        user = self.repository.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError(user_id)
        return user

    def patch_user(self,user_id:int,request:UserUpdate):
        user = self.get_user_by_id(user_id)

        if request.email is not None:

            existing_user = self.repository.get_by_email(request.email)

            if existing_user and existing_user.id != user_id:
                raise UserEmailAlreadyExists(request.email)

        return self.repository.update(user, request)
    def change_password(self,user_id:int, request:UserChangePassword):
        user = self.get_user_by_id(user_id)
        if not verify_password(request.current_password,user.password):
            raise WrongCurrentPassword
        new_password = hash_password(request.new_password)
        return self.repository.update_password(user,new_password)

    def delete_user(self,
                    user_id:int) -> None:
        user = self.get_user_by_id(user_id)
        self.repository.delete_user(user)
