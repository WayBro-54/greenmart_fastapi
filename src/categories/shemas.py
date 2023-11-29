from typing import Optional, List
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    title: str
    code: int
    description: Optional[str]
    country: Optional[str]


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
    description: Optional[str] = Field(None)
