from datetime import datetime

from databases.interfaces import Record
from sqlalchemy import insert, select

from src.database import database, student_messages, students
from src.messages.schemas import StudentMessageCreate


async def get_student_messages(id: int, limit: int = 10) -> Record | None:
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


async def create_student_message(data: StudentMessageCreate) -> Record | None:
    insert_query = (
        insert(student_messages)
        .values(
            message=data.message,
            student_id=data.student_id,
            created_at=datetime.utcnow(),
        )
        .returning(student_messages)
    )
    return await database.fetch_one(insert_query)
