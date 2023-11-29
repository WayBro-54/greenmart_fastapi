from typing import Optional
from pydantic import BaseModel, Field



class ProductCategory(BaseModel):
    id: Optional[int] = Field(None)
    title: Optional[str] = Field(None)
    code: Optional[str] = Field(None)


class ProductBase(BaseModel):
    title: str = Field(None)
    code: int = Field(None)


class ProductItem(ProductBase):
    id: int
    description: Optional[str]
    country: Optional[str]
    count: int


class ProductList(ProductBase):
    id: int
    description: Optional[str]
    country: Optional[str]
    count: int


class ProductCreate(ProductBase):
    description: Optional[str] = Field(None)
    country: Optional[str] = Field(None)
    count: Optional[int] = Field(None)
    categories: Optional[list[ProductCategory]] = Field(
        default_factory=list
    )


class ProductUpdate(ProductBase):
    description: Optional[str]
    # categories: list[ProductCategory]
    country: Optional[str]
    count: int


class ProductDB(ProductBase):
    id: int = Field(None)
    description: Optional[str] = Field(None)
    country: Optional[str] = Field(None)
    count: int = Field(None)


