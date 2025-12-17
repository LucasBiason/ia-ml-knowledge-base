"""
Chat service for business logic.
"""
from typing import Optional, List, AsyncGenerator
from sqlalchemy.orm import Session
from openai import OpenAI

from app.core.openai_client import get_openai_client
from app.models.chat import ChatSession, ChatMessage
from app.schemas.chat import MessageCreate, ChatRequest
from app.repositories.chat_repository import ChatRepository


class ChatService:
    """Service for chat operations."""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = ChatRepository(db)
        self.client: OpenAI = get_openai_client()
    
    def send_message(
        self,
        user_id: int,
        request: ChatRequest,
        model: Optional[str] = None
    ) -> dict:
        """
        Send a message and get response from OpenAI.
        
        Args:
            user_id: ID of the user sending the message
            request: Chat request with message and parameters
            model: Model to use (defaults to config)
            
        Returns:
            dict: Response with message and session info
        """
        # Get or create session
        session = self.repository.get_or_create_session(
            user_id=user_id,
            session_id=request.session_id
        )
        
        # Save user message
        user_message = self.repository.create_message(
            session_id=session.id,
            role="user",
            content=request.message,
            message_type="text"
        )
        
        # Get conversation history
        messages = self.repository.get_session_messages(session.id)
        messages_for_api = [
            {"role": msg.role, "content": msg.content}
            for msg in messages[-10:]  # Last 10 messages for context
        ]
        
        # Call OpenAI API
        model = model or "gpt-3.5-turbo"
        response = self.client.chat.completions.create(
            model=model,
            messages=messages_for_api,
            temperature=request.temperature or 0.7,
            max_tokens=request.max_tokens
        )
        
        assistant_content = response.choices[0].message.content
        
        # Save assistant response
        assistant_message = self.repository.create_message(
            session_id=session.id,
            role="assistant",
            content=assistant_content,
            message_type="text"
        )
        
        return {
            "message": assistant_content,
            "session_id": session.id,
            "message_id": assistant_message.id
        }
    
    def stream_message(
        self,
        user_id: int,
        request: ChatRequest,
        model: Optional[str] = None
    ):
        """
        Stream message response from OpenAI.
        
        Args:
            user_id: ID of the user
            request: Chat request
            model: Model to use
            
        Yields:
            str: Chunks of the response
        """
        # Get or create session
        session = self.repository.get_or_create_session(
            user_id=user_id,
            session_id=request.session_id
        )
        
        # Save user message
        self.repository.create_message(
            session_id=session.id,
            role="user",
            content=request.message,
            message_type="text"
        )
        
        # Get conversation history
        messages = self.repository.get_session_messages(session.id)
        messages_for_api = [
            {"role": msg.role, "content": msg.content}
            for msg in messages[-10:]
        ]
        
        # Stream response
        model = model or "gpt-3.5-turbo"
        stream = self.client.chat.completions.create(
            model=model,
            messages=messages_for_api,
            temperature=request.temperature or 0.7,
            max_tokens=request.max_tokens,
            stream=True
        )
        
        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                full_response += content
                yield content
        
        # Save complete response
        self.repository.create_message(
            session_id=session.id,
            role="assistant",
            content=full_response,
            message_type="text"
        )

