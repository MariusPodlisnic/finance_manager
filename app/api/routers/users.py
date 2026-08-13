from uuid import UUID
from fastapi import APIRouter,Depends,Query,status
from app.api.deps import get_user_service
from app.api.responses import error_responses
from app.api.schemas.user_schemas import (
    UserUpdate,
    UserCreate,
    UserResponse
)
from app.services import user_service
from app.services.user_service import UserService

users_router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)

@users_router.get(
    "",
    response_model=UserResponse,
    summary="Get users",
    responses=error_responses(400,500)
)
def get_users(
        user_service:UserService = Depends(get_user_service)
    ) ->UserResponse:
    return user_service.get_users()
@users_router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Get user by id",
    responses=error_responses(400,404,500)
)
def get_user_by_id(
        user_id:UUID,
        user_service:UserService = Depends(get_user_service)
):
    return user_service.get_user_by_id(user_id)
@users_router.post(
    "",
    response_model=UserResponse,
    summary="Create user",
    responses=error_responses(400,409,500)
)
def create_user(
        user_data:UserCreate,
        user_service:UserService = Depends(get_user_service)
):
    return user_service.create_user(user_data)

@users_router.patch(
    "/{user_id}",
    response_model=UserResponse,
    summary="Update user",
    responses=error_responses(400,404,500)
)
def update_user(
        user_id:UUID,
        user_data:UserUpdate,
        user_service:UserService = Depends(get_user_service),
):
    return user_service.patch_user(user_id,user_data)

@users_router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user",
    responses=error_responses(404,500)
)
def delete_user(
        user_id:UUID,
        user_service:UserService = Depends(get_user_service)
):
    user_service.delete_user(user_id)
