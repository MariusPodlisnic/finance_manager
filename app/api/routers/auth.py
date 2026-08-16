from fastapi import APIRouter,Response,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import User
from app.utils.password import verify_password
from app.core.security import create_token

login_router = APIRouter(tags=['Authentication'])

@login_router.post("/login",status_code=status.HTTP_202_ACCEPTED)
def login(user_credentials:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")
    if not verify_password(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")

    access_token = create_token(data={"email":user.email})
    return {"token":access_token,"token_type":"bearer"}

