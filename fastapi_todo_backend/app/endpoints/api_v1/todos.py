from typing import Any
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.db import get_session
from app.models.todo import Todo
from app.schema.todo import TodoCreate, TodoRead

router = APIRouter()


@router.get('/')
async def read_todos():
    return ["Todo1", "Todo2", "Todo3"]


@router.post('', response_model=TodoRead)
def create_hero(*, session: Session = Depends(get_session), todo: TodoCreate):
    db_hero = Todo.from_orm(todo)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero
