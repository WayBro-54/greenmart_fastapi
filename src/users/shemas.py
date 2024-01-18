import uuid

from pydantic import BaseModel
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class AgentDB(BaseModel):
    pass


class AgentUpdate(BaseModel):
    pass


class AgentDelete(BaseModel):
    pass
