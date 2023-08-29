from fastapi import APIRouter
from src.students.schemas import StudentUpdate

from src.students import service
from src.students.schemas import Student

router = APIRouter()


@router.get("/students")
async def get_students() -> list[Student]:
    students = await service.get_students()
    return students

@router.patch("/students/{student_id}", response_model=StudentUpdate)
async def update_student(student_id: int, student: StudentUpdate) -> StudentUpdate:
    updated_student = await service.update_student(student_id, student)
    return updated_student
