from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repositories import user_repository
from app.repositories.user_repository.sqlalchemy_user_repository import SqlAlchemyUserRepository
from app.services.user_service import UserService
from app.utils.password import oauth2_scheme,password_context
from app.core.security import verify_access_token
from app.db.models import User

def get_user_service(
        db:Session = Depends(get_db)
) -> UserService:
    user_repository = SqlAlchemyUserRepository(db)
    return UserService(user_repository)


def get_current_user(token:str = Depends(oauth2_scheme),db:Session = Depends(get_db)):
    token = verify_access_token(token)
    user = db.query(User).filter(User.email == token.email).first()

    return user