from databases.interfaces import Record
from src.students.schemas import StudentUpdate

from src.database import database, students
from src.students.schemas import Student


async def get_students() -> Record | None:
    select_query = students.select().order_by(students.c.id)
    result = await database.fetch_all(select_query)
    rows = [dict(row) for row in result]
    return [Student(**row) for row in rows]

async def get_student(student_id: int) -> Student | None:
    select_query = students.select().where(students.c.id == student_id)
    result = await database.fetch_one(select_query)
    if result is None:
        return None
    return Student(**dict(result))

async def update_student(student_id: int, student: StudentUpdate) -> StudentUpdate | None:
    update_query = students.update().where(students.c.id == student_id).values(**student.model_dump(exclude_none=True))
    await database.execute(update_query)
    return student
   
