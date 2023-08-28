from src.database import database, students
from databases.interfaces import Record

from src.students.schemas import Student


async def get_students() -> Record | None:
    select_query = students.select().order_by(students.c.id)
    result = await database.fetch_all(select_query)
    rows = [dict(row) for row in result]
    return [
        Student(
            **row
        ) for row in rows
    ]
