from fastapi import FastAPI
from app.api.routers.users import users_router

app = FastAPI(title="Finance managing API")

app.include_router(users_router)

