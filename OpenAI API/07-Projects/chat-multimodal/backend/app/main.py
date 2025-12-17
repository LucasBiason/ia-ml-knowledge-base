"""
Main FastAPI application.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1 import chat, vision, audio

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Chat Multimodal API with OpenAI integration"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router, prefix=settings.API_V1_PREFIX)
app.include_router(vision.router, prefix=settings.API_V1_PREFIX)
app.include_router(audio.router, prefix=settings.API_V1_PREFIX)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Chat Multimodal API",
        "version": settings.VERSION,
        "docs": "/docs"
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}

