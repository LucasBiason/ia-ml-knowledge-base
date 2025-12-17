"""
Application configuration using Pydantic Settings.
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # API
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "Chat Multimodal API"
    VERSION: str = "1.0.0"

    # OpenAI
    OPENAI_API_KEY: str

    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost/chat_multimodal"

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:3001"]

    # File Upload
    MAX_UPLOAD_SIZE: int = 25 * 1024 * 1024  # 25 MB
    ALLOWED_IMAGE_TYPES: list[str] = ["image/jpeg", "image/png", "image/webp"]
    ALLOWED_AUDIO_TYPES: list[str] = ["audio/mpeg", "audio/wav", "audio/mp4", "audio/webm"]

    # OpenAI Models
    DEFAULT_CHAT_MODEL: str = "gpt-3.5-turbo"
    VISION_MODEL: str = "gpt-4-vision-preview"
    TRANSCRIPTION_MODEL: str = "whisper-1"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()





