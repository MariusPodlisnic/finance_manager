from __future__ import annotations
from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy import select,func

from app.api.schemas.user_schemas import UserUpdate
from app.db.models import User
from app.repositories.user_repository.base import UserRepository
from app.exceptions.user_exceptions import UserNotFoundError

class SqlAlchemyUserRepository(UserRepository):
    def __init__(self,db:Session):
        self.db = db

    def get_users(
            self) -> list[User]:
        statement = select(User)
        return list(self.db.scalars(statement))

    def create(self,data:User) -> User:
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)

        return data

    def get_by_id(self,user_id:UUID) -> User | None:
        statement = select(User).where(User.id == user_id)
        user = self.db.scalar(statement)
        return user

    def get_by_email(self,email:str) -> User | None:
        statement = select(User).where(func.lower(User.email) == email.lower())
        user = self.db.scalar(statement)
        return user

    def update(self,user:User,data:UserUpdate) -> User:
        updated_data = data.model_dump(exclude_unset=True)
        for field,value in updated_data.items():
            setattr(user,field,value)

        self.db.commit()
        self.db.refresh(user)

        return user

    def delete_user(self,user:User) -> None:
        self.db.delete(user)
        self.db.commit()
