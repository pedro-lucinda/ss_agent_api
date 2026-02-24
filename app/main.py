from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes import (
    chat
)
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        openapi_url=f"{settings.api_prefix}/openapi.json",
        docs_url=f"{settings.api_prefix}/docs",
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.backends_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
   
    app.include_router(
        chat.router,
        prefix=f"{settings.api_prefix}/chat",
        tags=["chat"],
    )

    return app


# Instantiate
app = create_app()
