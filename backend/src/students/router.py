from fastapi import APIRouter

from src.exceptions import NotFound
from src.students import service
from src.students.schemas import Student, StudentCreate, StudentUpdate

router = APIRouter()


@router.get("/students")
async def get_students() -> list[Student]:
    students = await service.get_students()
    return students


@router.get("/students/{student_id}")
async def get_student(student_id: int) -> Student:
    student = await service.get_student_and_messages(student_id)
    if student is None:
        raise NotFound()
    return student


@router.post("/students", response_model=Student)
async def create_student(student: StudentCreate) -> Student:
    new_student = await service.create_student(student)
    return new_student


@router.patch("/students/{student_id}", response_model=StudentUpdate)
async def update_student(student_id: int, student: StudentUpdate) -> StudentUpdate:
    updated_student = await service.update_student(student_id, student)
    return updated_student
