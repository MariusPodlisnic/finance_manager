from fastapi import FastAPI
from app.api.routers.users import users_router
from app.api.routers.auth import login_router
app = FastAPI(title="Finance managing API")

app.include_router(users_router)
app.include_router(login_router)

