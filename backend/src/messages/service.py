from datetime import datetime
from typing import Any, Mapping

from sqlalchemy import func, insert, select, text, update

from src.database import Student as students
from src.database import StudentMessage as student_messages
from src.database import execute, fetch_all, fetch_raw_all, fetch_one
from src.messages.schemas import StudentMessageCreate, MarkMessagesRead


async def get_student_messages(id: int, limit: int = 10) -> list[Mapping]:
    query_raw = """
    SELECT id, message, created_at, message_type, 'student' as sender, is_read
    FROM student_messages
    WHERE student_id = :id
    UNION
    SELECT id, message, created_at, 'text' as message_type, 'sensei' as sender, true as is_read
    FROM sensei_messages
    WHERE student_id = :id
    ORDER BY created_at
    LIMIT :limit
    OFFSET :offset
    """
    return await fetch_raw_all(query_raw, {"id": id, "limit": limit, "offset": 0})


async def get_student_by_id(id: int) -> dict[str, Any] | None:
    select_query = select(students).where(students.id == id)
    result = await fetch_one(select_query)
    return result


async def create_student_message(data: StudentMessageCreate) -> list[Mapping] | None:
    insert_query = (
        insert(student_messages)
        .values(
            message=data.message,
            student_id=data.student_id,
            created_at=datetime.utcnow(),
            message_type=data.message_type,
            is_read=data.is_read,
        )
        .returning(student_messages)
    )
    return await fetch_one(insert_query)


async def get_unread_message_count() -> Mapping | None:
    select_query = select(func.count(student_messages.id).label("count")).where(
        student_messages.is_read == False  # noqa
    )
    result = await fetch_one(select_query)

    return {
        "count": result["count"],
    }


async def get_all_unread_messages() -> list[Mapping] | None:
    select_query = (
        select(student_messages)
        .where(student_messages.is_read == False)  # noqa
        .group_by(student_messages.student_id)
    )

    result = await fetch_all(select_query)
    return result


async def mark_as_read(messages: MarkMessagesRead) -> None:
    update_query = (
        update(student_messages)
        .where(student_messages.id.in_(messages.message_ids))
        .where(student_messages.is_read == False) # noqa
        .values(is_read=True)
    )
    await execute(update_query)
