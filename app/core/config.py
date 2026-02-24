from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()


def _parse_cors_origins(v: str) -> list[str]:
    """Parse '*' or comma-separated origins from env."""
    if not v or v.strip() == "*":
        return ["*"]
    return [o.strip() for o in v.split(",") if o.strip()]


class Settings(BaseSettings):
    """Application settings from environment or .env."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    app_name: str = Field(default="Smoking Assistant", validation_alias="APP_NAME")
    api_prefix: str = Field(default="/api/v1", validation_alias="API_PREFIX")
    cors_origins_env: str = Field(
        default="http://localhost:3000,http://localhost:8000",
        validation_alias="BACKENDS_CORS_ORIGINS",
    )
    openai_api_key: str = Field(..., validation_alias="OPENAI_API_KEY")
    # tavily_api_key: str = Field(..., validation_alias="TAVILY_API_KEY")
    database_url: str = Field(..., validation_alias="DATABASE_URL")
    debug: bool = Field(default=False, validation_alias="DEBUG")

    @computed_field
    @property
    def backends_cors_origins(self) -> list[str]:
        return _parse_cors_origins(self.cors_origins_env)

    def model_post_init(self, __context: Any) -> None:
        # Use async driver for SQLAlchemy async engine
        if self.database_url.startswith(("postgresql://", "postgresql+psycopg2://")):
            self.database_url = self.database_url.replace(
                "postgresql+psycopg2://", "postgresql+asyncpg://", 1
            ).replace("postgresql://", "postgresql+asyncpg://", 1)


settings = Settings()
