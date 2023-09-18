from fastapi import APIRouter
from src.langchain import service
router = APIRouter()


@router.get("/")
async def root():
    response = service.get_ai_response()
    return {"message": response}
