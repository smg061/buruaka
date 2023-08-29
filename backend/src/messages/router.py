from typing import Any

from fastapi import APIRouter, Depends

from src.messages import service

from src.messages.dependencies import valid_student_id
from src.messages.schemas import Message, StudentMessageCreate

router = APIRouter()


@router.get("/messages/{id}")
async def get_messages(id: int) -> list[Message]:
    res = await service.get_student_messages(id)
    print(res)
    return res


@router.post("/messages", response_model=StudentMessageCreate)
async def create_student_message(
    data: StudentMessageCreate = Depends(valid_student_id),
) -> Any:
    res = await service.create_student_message(data)
    return res
