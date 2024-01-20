import uuid

from datetime import date
from typing import Annotated
from pydantic import BaseModel
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class AgentDB(BaseModel):
    firstname: str | None
    lastname: str | None
    surname: str | None
    birthday: date | None
    phone: str | None
    address: str | None


class AgentCreate(BaseModel):
    firstname: str | None
    lastname: str | None
    surname: str | None
    birthday: date | None
    phone: str | None
    address: str | None


class AgentUpdate(BaseModel):
    pass


class AgentDelete(BaseModel):
    pass
