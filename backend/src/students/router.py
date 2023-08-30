from fastapi import APIRouter
from src.students.schemas import StudentUpdate, StudentCreate

from src.students import service
from src.students.schemas import Student

router = APIRouter()


@router.get("/students")
async def get_students() -> list[Student]:
    students = await service.get_students()
    return students

@router.post("/students", response_model=Student)
async def create_student(student: StudentCreate) -> Student:
    new_student = await service.create_student(student)
    return new_student

@router.patch("/students/{student_id}", response_model=StudentUpdate)
async def update_student(student_id: int, student: StudentUpdate) -> StudentUpdate:
    updated_student = await service.update_student(student_id, student)
    return updated_student
