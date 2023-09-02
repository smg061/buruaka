from datetime import datetime
from typing import Mapping

from databases.interfaces import Record

from src.database import (
    database,
    StudentMessage as student_messages,
    Student as students,
)
from src.students.schemas import Student, StudentCreate, StudentUpdate


async def get_students() -> Record | None:
    raw_query = """
    SELECT 
        student.id,
        student.first_name,
        student.last_name,
        student.email,
        student.profile_picture,
        student.sprite,
        student.dob,
        student.profile_message,
        student.relationship_level,
        student.phone_number,
        array_remove(array_agg(it.message), NULL) as unread_messages
    FROM students as student
    LEFT JOIN (
        SELECT student_id, created_at, is_read, (
            CASE
                WHEN message_type = 'text' THEN message
                ELSE '[image]'
            END
        ) as message
        FROM student_messages
        WHERE is_read = false
        ORDER BY created_at
    ) as it
    ON it.student_id = student.id
    GROUP BY student.id
    """

    result = await database.fetch_all(raw_query)
    rows = [dict(row) for row in result]
    return [Student(**row) for row in rows]


async def get_student(student_id: int) -> Student | None:
    select_query = (
        students.select()
        .where(students.id == student_id)
        .join(student_messages, students.id == student_messages.student_id)
    )
    result = await database.fetch_one(select_query)
    return Student(**dict(result))


async def get_student_and_messages(student_id: int) -> Student | None:
    raw_query = """
        SELECT student.id, student.first_name,student.last_name, student.email
            ,student.profile_picture
            , student.sprite
            , student.dob
            , student.profile_message
            , student.relationship_level
            , student.phone_number
            , student_messages.last_message
        FROM students as student
        LEFT JOIN  (
            SELECT student_id, message as last_message
            FROM student_messages
        ) as student_messages
        ON student.id = student_messages.student_id
        WHERE student.id = :student_id
    """
    result = await database.fetch_one(raw_query, values={"student_id": student_id})
    if result is None:
        return None
    print(dict(result))
    return Student(**result)


async def create_student(student: StudentCreate) -> Mapping:
    insert_query = (
        students.insert()
        .values(
            {
                "first_name": student.first_name,
                "last_name": student.last_name,
                "email": student.email,
                "profile_picture": student.profile_picture,
                "sprite": student.sprite,
                "dob": datetime.strptime(student.dob, "%Y-%m-%d"),
                "profile_message": student.profile_message,
                "relationship_level": student.relationship_level,
                "phone_number": student.phone_number,
            }
        )
        .returning(students)
    )
    results = await database.fetch_one(insert_query)
    return results


async def update_student(student_id: int, student: StudentUpdate) -> Mapping | None:
    update_query = (
        students.update()
        .where(students.id == student_id)
        .values(**student.model_dump(exclude_none=True))
    )
    await database.execute(update_query)
    return await get_student(student_id)
