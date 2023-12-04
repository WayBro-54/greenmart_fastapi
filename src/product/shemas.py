from typing import Optional, Any
from pydantic import BaseModel, Field, validator


class ProductCategory(BaseModel):
    id: Optional[int] = Field(None)
    title: Optional[str] = Field(None)
    code: Optional[str] = Field(None)


class ProductBase(BaseModel):
    title: Optional[str] = Field(None)
    code: Optional[int] = Field(None)
    is_deleted: Optional[int] = Field(
        0,
        gt=0,
        lt=1,
    )

    def validator_is_deleted(self):
        pass



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
    categories: Optional[list[ProductCategory]]
    country: Optional[str]
    count: int


class ProductDB(BaseModel):
    id: Optional[int] = Field(None)
    title: Optional[str] = Field(None)
    code: Optional[int] = Field(None)
    # categories: Optional[list[ProductCategory]]


class ProductResponseModel(BaseModel):
    id: Any
    title: Any
    code: Any
