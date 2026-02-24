import os
from pathlib import Path
from typing import Any, List

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings, Field

# BASE_DIR is one level above app/
BASE_DIR = Path(__file__).resolve().parent.parent

# load the .env in your project root
load_dotenv()


class Settings(BaseSettings):
    """
    Application settings, loaded from environment or .env file.
    """

    app_name: str = os.getenv("APP_NAME", "Chef Agent")
    api_prefix: str = os.getenv("API_PREFIX", "/api/v1")
    backends_cors_origins: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000"],
        env="BACKENDS_CORS_ORIGINS",
    )

    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    tavily_api_key: str = Field(..., env="TAVILY_API_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        if not self.sqlalchemy_database_uri:
            self.sqlalchemy_database_uri = (
                f"postgresql://{self.postgres_user}:"
                f"{self.postgres_password}@{self.postgres_server}:5432/"
                f"{self.postgres_db}"
            )


# instantiate once
settings = Settings()
