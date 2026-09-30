from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repositories.user_repository.sqlalchemy_user_repository import SqlAlchemyUserRepository
from app.repositories.account_repository.sqlalchemy_account_repository import SqlAlchemyAccountRepository
from app.services.user_service import UserService
from app.services.account_service import AccountService
from app.utils.password import oauth2_scheme
from app.core.security import verify_access_token


def get_user_service(
        db:Session = Depends(get_db)
) -> UserService:
    user_repository = SqlAlchemyUserRepository(db)
    return UserService(user_repository)

def get_account_service(
        db:Session = Depends(get_db)
) -> AccountService:
    account_repository = SqlAlchemyAccountRepository(db)
    return AccountService(account_repository)

def get_current_user(token:str = Depends(oauth2_scheme)):
    token = verify_access_token(token)
    return {"email":token.email, "user_id":token.user_id, "role":token.role}