from fastapi import FastAPI

from config import settings
from routers import main_router

app = FastAPI(title=settings.title)

app.include_router(main_router)
