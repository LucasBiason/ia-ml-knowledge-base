"""
Chat API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import Optional

from app.core.database import get_db
from app.schemas.chat import ChatRequest, ChatResponse, ChatHistoryResponse
from app.services.chat_service import ChatService
from app.middleware.auth import get_current_user_id

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/message", response_model=ChatResponse)
async def send_message(
    request: ChatRequest,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    """
    Send a message and get response.
    
    Args:
        request: Chat request with message and parameters
        db: Database session
        user_id: Current user ID (from auth)
        
    Returns:
        ChatResponse: Response with message and session info
    """
    service = ChatService(db)
    result = service.send_message(user_id, request)
    return ChatResponse(**result)


@router.post("/stream")
async def stream_message(
    request: ChatRequest,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    """
    Stream message response.
    
    Args:
        request: Chat request
        db: Database session
        user_id: Current user ID
        
    Returns:
        StreamingResponse: SSE stream of response chunks
    """
    service = ChatService(db)
    
    async def generate():
        for chunk in service.stream_message(user_id, request):
            yield f"data: {chunk}\n\n"
        yield "data: [DONE]\n\n"
    
    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )


@router.get("/sessions")
async def get_sessions(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    """
    Get all chat sessions for the current user.
    
    Args:
        db: Database session
        user_id: Current user ID
        
    Returns:
        List of chat sessions
    """
    service = ChatService(db)
    sessions = service.repository.get_user_sessions(user_id)
    return sessions


@router.get("/history/{session_id}")
async def get_history(
    session_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    """
    Get chat history for a session.
    
    Args:
        session_id: ID of the session
        db: Database session
        user_id: Current user ID
        
    Returns:
        ChatHistoryResponse: Session and messages
    """
    service = ChatService(db)
    session = service.repository.get_or_create_session(user_id, session_id)
    
    if session.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this session"
        )
    
    messages = service.repository.get_session_messages(session_id)
    return ChatHistoryResponse(session=session, messages=messages)


@router.delete("/sessions/{session_id}")
async def delete_session(
    session_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    """
    Delete a chat session.
    
    Args:
        session_id: ID of the session
        db: Database session
        user_id: Current user ID
        
    Returns:
        dict: Success message
    """
    service = ChatService(db)
    deleted = service.repository.delete_session(session_id, user_id)
    
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    return {"message": "Session deleted successfully"}

