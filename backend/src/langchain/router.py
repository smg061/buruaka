from fastapi import APIRouter
from src.langchain import service
router = APIRouter()


@router.get("/")
async def root():
    response = service.get_ai_response('Hello')
    return {"message": response}

@router.post("/")
async def get_ai_student_response(body: dict[str, str]):
    response = service.get_ai_response(body['message'])
    return {"message": response}