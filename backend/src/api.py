from contextlib import asynccontextmanager
from typing import AsyncGenerator

import sentry_sdk
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.auth.router import router as auth_router
from src.config import app_configs, settings
from src.messages.router import router as messages_router
from src.students.router import router as students_router
from src.langchain.router import router as langchain_router


@asynccontextmanager
async def lifespan(_application: FastAPI) -> AsyncGenerator:
    # Startup
    yield
    # Shutdown


app = FastAPI(**app_configs, lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_origin_regex=settings.CORS_ORIGINS_REGEX,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=settings.CORS_HEADERS,
)

# if settings.ENVIRONMENT.is_deployed:
#     sentry_sdk.init(
#         dsn=settings.SENTRY_DSN,
#         environment=settings.ENVIRONMENT,
#     )


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(messages_router, prefix="/api/v1", tags=["Messages"])
app.include_router(students_router, prefix="/api/v1", tags=["Students"])
app.include_router(langchain_router, prefix="/api/v1/ai", tags=["AI Responses"])