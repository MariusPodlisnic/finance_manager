from __future__ import annotations

from typing import Protocol
from uuid import UUID

from app.db.models import User
from app.api.schemas.user_schemas import UserUpdate

class UserRepository(Protocol):
    def get_users(
            self) -> list[User]: ...

    def create(self,data:User) -> User: ...

    def get_by_id(self,user_id:UUID) -> User | None: ...

    def get_by_email(self,email:str) -> User | None: ...

    def update(self,user:User,data:UserUpdate) -> User: ...

    def delete_user(self,user:User) -> None: ...

