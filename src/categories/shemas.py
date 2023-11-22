from typing import Optional
from pydantic import BaseModel, Field


class CategoryItem(BaseModel):
    id: int
    code: str
    title: str
    description: str


class CategoryUpdate(BaseModel):
    code: Optional[str] = Field(None)
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)


class CategoryCreate(BaseModel):
    code: str
    title: str
    description: Optional[str] = Field(None)


class CategoryDB(BaseModel):
    id: int
    code: str
    title: str
    description: Optional[str]

