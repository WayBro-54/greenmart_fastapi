from typing import Optional, Any
from pydantic import BaseModel, Field


class ProductCategory(BaseModel):
    id: Optional[int] = Field(None)
    # title: Optional[str] = Field(None)
    # code: Optional[str] = Field(None)
    # class Config:
    #     orm_mode = True


class ProductBase(BaseModel):
    title: Optional[str] = Field(None)
    code: Optional[int] = Field(None)

    # class Config:
    #     orm_mode = True


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


class ProductDB(BaseModel):
    id: Optional[int] = Field(None)
    title: Optional[str] = Field(None)
    code: Optional[int] = Field(None)
    # description: Optional[str] = Field(None)
    # country: Optional[str] = Field(None)
    # count: Optional[int] = Field(None)


class ProductResponseModel(BaseModel):
    id: Any
    title: Any
    code: Any
