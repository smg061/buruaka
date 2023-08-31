from datetime import datetime
from typing import Mapping

from databases.interfaces import Record
from sqlalchemy import func, insert, select

from src.database import database, student_messages, students
from src.messages.schemas import StudentMessageCreate


async def get_student_messages(id: int, limit: int = 10) -> list[Mapping]:
    query_raw = """
    SELECT message, created_at, 'student' as sender
    FROM student_messages
    WHERE student_id = :id
    UNION
    SELECT message, created_at, 'sensei' as sender
    FROM sensei_messages
    WHERE student_id = :id
    ORDER BY created_at
    """
    return await database.fetch_all(query_raw, values={"id": id})


async def get_student_by_id(id: int) -> Record | None:
    select_query = select(students).where(students.c.id == id)
    result = await database.fetch_one(select_query)
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
    return await database.fetch_one(insert_query)


async def get_unread_message_count() -> Mapping | None:
    select_query = select(func.count(student_messages.c.id)).where(
        student_messages.c.is_read == False  # noqa
    )
    result = await database.execute(select_query)
    return {
        "count": result,
    }


async def get_all_unread_messages() -> list[Mapping] | None:
    select_query = select(student_messages).where(
        student_messages.c.is_read == False  # noqa
    ).group_by(student_messages.c.student_id)
    
    result = await database.fetch_all(select_query)
    return result
