from pydantic import EmailStr, PostgresDsn, SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: SecretStr
    db_url: PostgresDsn
    db_url_async: PostgresDsn
    prod: bool = False
    pgadmin_user: EmailStr
    pgadmin_password: SecretStr
    sqlite: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings()

if config.sqlite:
    db_url = "sqlite+aiosqlite:///db.sqlite3"
    config.db_url = db_url
    config.db_url_async = db_url
