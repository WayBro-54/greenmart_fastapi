from sqlalchemy import Column, Boolean, String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column
from scr.core.base import Base


class Category(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(30))
    title: Mapped[str] = mapped_column(String(250))
    description: Mapped[str]
    
