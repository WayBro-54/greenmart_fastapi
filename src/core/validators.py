from fastapi import HTTPException, status

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
        user: Users,
    ):
        if user.is_superuser:
            return user
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'{user.email}, is not superuser!',
        )