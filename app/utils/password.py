from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def hash_password(password:str):
    return password_context.hash(password)

def verify_password(plain_password:str,hashed_password:str):
    return password_context.verify(plain_password,hashed_password)