from datetime import datetime, timedelta
import jwt
from jwt.exceptions import InvalidTokenError
from app.api.schemas.login_schemas import TokenData
from app.core.config import settings
from app.exceptions.login_exceptions import WrongCredentials

SECRET_KEY = f"{settings.secret_key}"
ALGORITHM = f"{settings.algorithm}"
TOKEN_EXPIRE = f"{settings.token_expire}"


def create_token(data:dict):
    to_encode = data.copy()
    expire_time = datetime.utcnow() + timedelta(minutes=int(TOKEN_EXPIRE))
    to_encode.update({"exp":expire_time})
    jwt_token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return jwt_token

def verify_access_token(token:str):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email:str = payload.get("email")
        if not email:
            raise WrongCredentials
        return TokenData(email=email)
    except InvalidTokenError:
        raise WrongCredentials



