from fastapi import APIRouter,Depends,status
from app.api.deps import get_current_user,get_account_service
from app.api.responses import error_responses
from app.api.schemas.account_schemas import AccountResponse, AccountCreate, AccountUpdate
from app.services.account_service import AccountService

account_router = APIRouter(
    prefix="/api/account",
    tags=["Account"]
)

@account_router.get(
    "/{user_id)",
    response_model=list[AccountResponse],
    summary="Get accounts",
    responses=error_responses(400,500)
)
def get_accounts(
        user_id: int,
        account_service: AccountService = Depends(get_account_service),
        current_user:str = Depends(get_current_user)
) -> AccountResponse:
    return account_service.get_accounts(user_id)

@account_router.post(
    "/{user_id}",
    response_model=AccountResponse,
    summary="Create new account",
    responses=error_responses(400,500)
)

def create_account(
        user_id: int,
        data: AccountCreate,
        account_service: AccountService = Depends(get_account_service),
        current_user: str = Depends(get_current_user)
) -> AccountResponse:
    return account_service.create_account(user_id,data)

@account_router.patch(
    "/{user_id}",
    response_model=AccountResponse,
    summary="Update account",
    responses=error_responses(400,500)
)

def update_account(
        user_id: int,
        account_id: int,
        data: AccountUpdate,
        account_service: AccountService = Depends(get_account_service),
        current_user: str = Depends(get_current_user)
) -> AccountResponse:
    return account_service.update_account(user_id,account_id,data)

@account_router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete account",
    responses=error_responses(404, 500)
)

def delete_account(
        user_id: int,
        account_id: int,
        account_service: AccountService = Depends(get_account_service),
        current_user: str = Depends(get_current_user)
):
    account_service.delete_account(user_id,account_id)




