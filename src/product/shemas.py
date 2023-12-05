from typing import Optional
from pydantic import BaseModel, Field, field_validator



class ProductCategory(BaseModel):
    id: Optional[int] = Field(None)
    title: Optional[str] = Field(None)
    code: Optional[str] = Field(None)
    # @field_validator()
    # @classmethod
    # def validate(cls: type[Model], value: Any) -> Model:


class ProductBase(BaseModel):
    title: Optional[str] = Field(None)
    code: Optional[int] = Field(None)
    description: Optional[str]
    count: int
    @field_validator('code')
    @classmethod
    def validate_code(cls, value):
        if not isinstance(value, int):
            raise ValueError(f'Code - целочисленное значение. code: [{value}]')
        return value


class ProductItem(ProductBase):
    id: int
    country: Optional[str]
    is_deleted: Optional[int] = Field(
        0,
        ge=0,
        le=1,
    )


class ProductList(ProductBase):
    id: int
    country: Optional[str]
    is_deleted: Optional[int] = Field(
        0,
        ge=0,
        le=1,
    )


class ProductCreate(ProductBase):
    country: Optional[str] = Field(None)
    categories: Optional[list[ProductCategory]] = Field(
        default_factory=list
    )


class ProductUpdate(ProductBase):
    categories: Optional[list[ProductCategory]]
    country: Optional[str]


class ProductDB(BaseModel):
    id: Optional[int] = Field(None)
    country: Optional[str]
    is_deleted: Optional[int] = Field(
        0,
        ge=0,
        le=1,
    )
    categories: Optional[list[ProductCategory]]
