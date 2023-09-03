from sqlmodel import SQLModel


class TodoCreate(SQLModel):
    title: str
    is_completed: bool = False


class TodoRead(SQLModel):
    id: int
    title: str
    is_completed: bool
