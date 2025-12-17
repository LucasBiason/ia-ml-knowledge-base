"""
Chat repository for data access.
"""
from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.models.chat import ChatSession, ChatMessage


class ChatRepository:
    """Repository for chat data access."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_or_create_session(
        self,
        user_id: int,
        session_id: Optional[int] = None
    ) -> ChatSession:
        """
        Get existing session or create new one.
        
        Args:
            user_id: ID of the user
            session_id: Optional session ID to retrieve
            
        Returns:
            ChatSession: Session object
        """
        if session_id:
            session = self.db.query(ChatSession).filter(
                ChatSession.id == session_id,
                ChatSession.user_id == user_id
            ).first()
            if session:
                return session
        
        # Create new session
        session = ChatSession(user_id=user_id)
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session
    
    def create_message(
        self,
        session_id: int,
        role: str,
        content: str,
        message_type: str = "text",
        metadata: Optional[dict] = None
    ) -> ChatMessage:
        """
        Create a new chat message.
        
        Args:
            session_id: ID of the session
            role: Role of the message (user, assistant, system)
            content: Message content
            message_type: Type of message (text, image, audio)
            metadata: Additional metadata
            
        Returns:
            ChatMessage: Created message
        """
        message = ChatMessage(
            session_id=session_id,
            role=role,
            content=content,
            message_type=message_type,
            metadata=metadata
        )
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return message
    
    def get_session_messages(
        self,
        session_id: int,
        limit: Optional[int] = None
    ) -> List[ChatMessage]:
        """
        Get messages for a session.
        
        Args:
            session_id: ID of the session
            limit: Optional limit on number of messages
            
        Returns:
            List[ChatMessage]: List of messages
        """
        query = self.db.query(ChatMessage).filter(
            ChatMessage.session_id == session_id
        ).order_by(ChatMessage.created_at)
        
        if limit:
            query = query.limit(limit)
        
        return query.all()
    
    def get_user_sessions(self, user_id: int) -> List[ChatSession]:
        """
        Get all sessions for a user.
        
        Args:
            user_id: ID of the user
            
        Returns:
            List[ChatSession]: List of sessions
        """
        return self.db.query(ChatSession).filter(
            ChatSession.user_id == user_id
        ).order_by(desc(ChatSession.updated_at)).all()
    
    def delete_session(self, session_id: int, user_id: int) -> bool:
        """
        Delete a session.
        
        Args:
            session_id: ID of the session
            user_id: ID of the user (for authorization)
            
        Returns:
            bool: True if deleted, False if not found
        """
        session = self.db.query(ChatSession).filter(
            ChatSession.id == session_id,
            ChatSession.user_id == user_id
        ).first()
        
        if session:
            self.db.delete(session)
            self.db.commit()
            return True
        return False

