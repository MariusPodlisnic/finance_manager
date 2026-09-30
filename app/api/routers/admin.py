from fastapi import APIRouter,Depends
from app.api.deps import get_user_service, get_current_user
from app.api.responses import error_responses
from app.api.schemas.user_schemas import (
    UserResponse
)
from app.exceptions.login_exceptions import NotAuthenticated
from app.services.user_service import UserService

admin_router = APIRouter(
    prefix="/api/admin",
    tags=["admin"]
)

@admin_router.get(
    "",
    response_model=list[UserResponse],
    summary="Get users",
    responses=error_responses(400,500)
)
def get_users(
        user_service:UserService = Depends(get_user_service),
        current_user = Depends(get_current_user)
    ) ->UserResponse:
    if not current_user or current_user.get("role") != "admin":
        raise NotAuthenticated
    return user_service.get_users()