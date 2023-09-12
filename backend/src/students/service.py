from datetime import datetime
from typing import Any, Mapping

from sqlalchemy import text

from src.database import Student as students
from src.database import StudentMessage as student_messages
from src.database import execute, fetch_all, fetch_one
from src.students.schemas import Student, StudentCreate, StudentUpdate


async def get_students() -> dict[str, Any] | None:
    raw_query = """
WITH last_five_messages AS
    (SELECT id,
            student_id,
            message,
            created_at,
            'student' AS sender,
            message_type,
            is_read
    FROM
        (SELECT id,
                student_id,
                (
                    CASE
                        WHEN message_type = 'text' THEN message
                        ELSE '[picture]'
                    END
                ) AS message,
                created_at,
                message_type,
                is_read,
                ROW_NUMBER() OVER(PARTITION BY student_id
                                ORDER BY created_at DESC) AS rn
        FROM public.student_messages) sub
    WHERE sub.rn <= 5
    UNION ALL SELECT    id,
                        student_id,
                        message,
                        created_at,
                        'sensei' AS sender,
                        'text' AS message_type,
                        true as is_read
    FROM
        (SELECT id,
                student_id,
                message,
                created_at,
                ROW_NUMBER() OVER(PARTITION BY student_id
                                ORDER BY created_at DESC) AS rn
        FROM public.sensei_messages) sub
    WHERE sub.rn <= 5 )
    SELECT s.id,
        s.first_name,
        s.last_name,
        s.email,
        s.profile_picture,
        s.sprite,
        s.dob,
        s.profile_message,
        s.relationship_level,
        s.phone_number,
        COALESCE(json_agg(json_build_object('message', m.message, 'is_read', m.is_read)) FILTER (
                                                                                                    WHERE m.message IS NOT NULL), '[]') AS messages
    FROM public.students s
    LEFT JOIN last_five_messages m ON m.student_id = s.id
    GROUP BY s.id;
"""

    result = await fetch_all(text(raw_query))
    rows = [dict(row) for row in result]
    return [Student(**row) for row in rows]


async def get_student(student_id: int) -> Student | None:
    select_query = (
        students.select()
        .where(students.id == student_id)
        .join(student_messages, students.id == student_messages.student_id)
    )
    result = await fetch_one(select_query)
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
    result = await fetch_one(text(raw_query), values={"student_id": student_id})
    if result is None:
        return None
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
    results = await fetch_one(insert_query)
    return results


async def update_student(student_id: int, student: StudentUpdate) -> Mapping | None:
    update_query = (
        students.update()
        .where(students.id == student_id)
        .values(**student.model_dump(exclude_none=True))
    )
    await execute(update_query)
    return await get_student(student_id)
