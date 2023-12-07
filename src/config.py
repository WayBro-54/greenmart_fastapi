from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import EmailStr


class Settings(BaseSettings):
    title: str = 'Greenmart'
    db_url: str = 'postgresql+asyncpg://dev:def@localhost:5432/greenmart'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None
    jwt_lifetime: Optional[int] = 3600
    format: Optional[str] = '%Y/%m/%d %H:%M:%S'
    format_log_file: Optional[str] = '%Y_%m_%d'

    class Config:
        env_file = '../.env'


settings = Settings()
