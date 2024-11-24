
# app/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .routes import router, health_router
from .logging_config import setup_logging
from .middleware import LoggingMiddleware
import logging

logger = setup_logging()


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="FastAPI Application",
        description="A well-structured FastAPI application template",
        version="1.0.0"
    )

    # Add logging middleware
    app.add_middleware(LoggingMiddleware)

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(health_router)
    app.include_router(router, prefix="/api/v1")

    @app.on_event("startup")
    async def startup_event():
        logger.info("Application startup", extra={'correlation_id': 'startup'})

    @app.on_event("shutdown")
    async def shutdown_event():
        logger.info("Application shutdown", extra={'correlation_id': 'shutdown'})

    return app


app = create_app()