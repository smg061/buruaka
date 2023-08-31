from enum import Enum
from typing import Any

from pydantic import PostgresDsn, root_validator
from pydantic_settings import BaseSettings


class Environment(str, Enum):
    LOCAL = "LOCAL"
    STAGING = "STAGING"
    TESTING = "TESTING"
    PRODUCTION = "PRODUCTION"

    @property
    def is_debug(self) -> bool:
        return self in (self.LOCAL, self.STAGING, self.TESTING)

    @property
    def is_testing(self) -> bool:
        return self == self.TESTING

    @property
    def is_deployed(self) -> bool:
        return self in (self.PRODUCTION, self.STAGING)


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn

    SITE_DOMAIN: str = "localhost:5173"

    ENVIRONMENT: Environment = Environment.LOCAL

    SENTRY_DSN: str | None = None

    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None
    CORS_HEADERS: list[str]

    APP_VERSION: str = "1"

    class Config:
        # env_file = ".env"
        extra = "ignore"

    @root_validator(skip_on_failure=True)
    def validate_sentry_non_local(cls, data: dict[str, Any]) -> dict[str, Any]:
        if data.get("ENVIRONMENT").is_deployed and not data.get("SENTRY_DSN"):
            raise ValueError("SENTRY_DSN is required for deployed environments")
        return data


settings = Settings()

app_configs: dict[str, Any] = {
    "title": "API",
}
if settings.ENVIRONMENT.is_deployed:
    app_configs["root_path"] = f"v/{settings.APP_VERSION}"

if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None  # hide docs
