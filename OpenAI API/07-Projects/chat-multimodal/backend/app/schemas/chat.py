"""
Chat schemas for request/response validation.
"""
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime


class MessageBase(BaseModel):
    """Base message schema."""
    role: Literal["system", "user", "assistant"]
    content: str
    message_type: Literal["text", "image", "audio"] = "text"


class MessageCreate(MessageBase):
    """Schema for creating a message."""
    session_id: Optional[int] = None
    image_url: Optional[str] = None
    audio_url: Optional[str] = None


class MessageResponse(MessageBase):
    """Schema for message response."""
    id: int
    session_id: int
    created_at: datetime
    metadata: Optional[dict] = None
    
    class Config:
        from_attributes = True


class ChatRequest(BaseModel):
    """Schema for chat request."""
    message: str
    session_id: Optional[int] = None
    stream: bool = False
    model: Optional[str] = None
    temperature: Optional[float] = Field(None, ge=0.0, le=2.0)
    max_tokens: Optional[int] = Field(None, gt=0)


class ChatResponse(BaseModel):
    """Schema for chat response."""
    message: str
    session_id: int
    message_id: int


class ChatSessionResponse(BaseModel):
    """Schema for chat session response."""
    id: int
    user_id: int
    title: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    message_count: int = 0
    
    class Config:
        from_attributes = True


class ChatHistoryResponse(BaseModel):
    """Schema for chat history response."""
    session: ChatSessionResponse
    messages: List[MessageResponse]





