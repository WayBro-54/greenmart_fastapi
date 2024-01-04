import uuid
from typing import Optional
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy
)
from config import settings

# async def get_user_manager(
#         user_db: SQL
# )
