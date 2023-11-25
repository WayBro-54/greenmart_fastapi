from typing import Optional, Any

from sqlalchemy import types, Dialect
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.type_api import _T


class NonNegativeInteger(types.TypeDecorator):
    impl = types.Integer

    def process_bind_param(self, value: Optional[_T], dialect: Dialect) -> None:
        if value is not None and value < 0:
            raise ValueError(f'Число [{value}], должно быть положительным')
        return value
