from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def read_todos():
    return ["Todo1", "Todo2", "Todo3"]
