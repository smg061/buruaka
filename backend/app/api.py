from fastapi import FastAPI

from app.routes.router import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")
