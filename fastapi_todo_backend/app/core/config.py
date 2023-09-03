import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DB_URL: str = Field(..., env='DATABASE_URL')
    # DB_URL: str = "postgresql://postgres:tareq888@localhost:5432/todos_db"

settings = Settings()
