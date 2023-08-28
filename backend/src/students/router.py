from fastapi import APIRouter
from src.students import service
from src.students.schemas import Student

router = APIRouter()


@router.get("/students")
async def get_students() -> list[Student]:
    students = await service.get_students()
    return students
