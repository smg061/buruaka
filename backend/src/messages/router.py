from fastapi import APIRouter, Depends

from src.messages import service
from src.messages.dependencies import valid_student_id
from src.messages.schemas import (Message, StudentMessageCount,
                                  StudentMessageCreate, MarkMessagesRead)

router = APIRouter()


@router.get("/messages/unread")
async def get_unread_message_count() -> StudentMessageCount:
    res = await service.get_unread_message_count()
    return res


@router.get("/messages/{id}")
async def get_messages(id: int) -> list[Message]:
    res = await service.get_student_messages(id)
    return res


@router.post("/messages", response_model=StudentMessageCreate)
async def create_student_message(
    data: StudentMessageCreate = Depends(valid_student_id),
) -> StudentMessageCreate:
    res = await service.create_student_message(data)
    return res


@router.post("/messages/mark-read")
async def mark_messages_read(messages: MarkMessagesRead) -> None:
    await service.mark_as_read(messages)
    