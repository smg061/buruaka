from typing import Any

from fastapi import APIRouter, Depends

from src.messages import service
from src.messages.dependencies import valid_student_id
from src.messages.schemas import Message, StudentMessageCreate

router = APIRouter()


@router.get("/messages/{id}")
async def get_messages(id: int) -> list[Message]:
    res = await service.get_student_messages(id)
    rows = [dict(row) for row in res]
    return [
        Message(
            message=row["message"],
            created_at=row["created_at"],
            sender=row["sender"],
            student_id=id,
        )
        for row in rows
    ]


@router.post("/messages")
async def create_student_message(
    data: StudentMessageCreate = Depends(valid_student_id),
) -> Any:
    res = await service.create_student_message(data)
    return Message(
        message=res["message"],
        created_at=res["created_at"],
        sender="student",
        student_id=res["student_id"],
    )
