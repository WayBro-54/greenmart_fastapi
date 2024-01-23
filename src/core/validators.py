from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from users.models import Users


class BaseValidation:
    def __init__(
        self,
        model,
        crud,
    ):
        self.model = model
        self.crud = crud

    async def is_superuser(
        self,
        _user: Users,
    ):
        if _user.is_superuser:
            return _user
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'{_user.email}, is not superuser!',
        )

    async def get_object_or_404(
            self,
            _id: int,
            _session: AsyncSession
    ):
        is_exist_db = await self.crud.get(
            _id,
            _session,
        )
        if is_exist_db is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Record with ID={_id}, dont detected!'
            )
        return is_exist_db
