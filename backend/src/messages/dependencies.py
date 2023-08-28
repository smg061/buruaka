from src.exceptions import BadRequest
from src.messages import service
from src.messages.schemas import StudentMessageCreate


async def valid_student_id(data: StudentMessageCreate) -> StudentMessageCreate:
    student = await service.get_student_by_id(data.student_id)
    if not student:
        raise BadRequest()
    return data
