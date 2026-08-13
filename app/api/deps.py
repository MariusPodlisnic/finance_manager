from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repositories import user_repository
from app.repositories.user_repository.sqlalchemy_user_repository import SqlAlchemyUserRepository
from app.services.user_service import UserService


def get_user_service(
        db:Session = Depends(get_db)
) -> UserService:
    user_repository = SqlAlchemyUserRepository(db)
    return UserService(user_repository)
