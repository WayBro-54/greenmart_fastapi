from pydantic import BaseModel

class CategoryItem(BaseModel):
    id: int
    code: str
    title: str
    description: str

