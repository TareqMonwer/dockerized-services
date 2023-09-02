from fastapi import APIRouter

from app.endpoints.api_v1 import (todos, )


api_router = APIRouter()

api_router.include_router(
  todos.router,
  prefix="/todos",
  tags=["Todos"]
)
