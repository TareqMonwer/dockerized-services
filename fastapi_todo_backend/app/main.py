from fastapi import FastAPI

from app.endpoints.api import api_router
from app.db.db import create_db_and_tables


create_db_and_tables()

app = FastAPI()

app.include_router(api_router, prefix="/api")
