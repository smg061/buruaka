from fastapi import FastAPI

from app.routes.router import router as api_router
from app.config import app_configs

app = FastAPI(**app_configs)

app.include_router(api_router, prefix="/api/v1")
