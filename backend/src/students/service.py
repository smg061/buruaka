from datetime import datetime
from typing import Mapping
from databases.interfaces import Record
from src.students.schemas import StudentCreate
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
    return Student(**dict(result))

async def create_student(student: StudentCreate) -> Mapping:
    insert_query = students.insert().values({
        "first_name": student.first_name,
        "last_name": student.last_name,
        "email": student.email,
        "profile_picture": student.profile_picture,
        "sprite": student.sprite,
        "dob": datetime.strptime(student.dob, '%Y-%m-%d'),
        "profile_message": student.profile_message,
        "relationship_level": student.relationship_level,
        "phone_number": student.phone_number,
    }).returning(students)
    results = await database.fetch_one(insert_query)
    return results

    
async def update_student(student_id: int, student: StudentUpdate) -> Mapping | None:
    update_query = students.update().where(students.c.id == student_id).values(**student.model_dump(exclude_none=True))
    await database.execute(update_query)
    try:
        return await get_student(student_id)
    except:
        return None
   
