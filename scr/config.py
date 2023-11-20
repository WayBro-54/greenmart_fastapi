from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    title: str = 'Greenmart'
    db_url: str = 'postgresql+asyncpg://dev:def@localhost:5432/greenmart'

    class Config:
        env_file = '../.env'


settings = Settings()
