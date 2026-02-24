from app.core.db.base import Base
from sqlalchemy import Column, ForeignKey, UUID, TIMESTAMP, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

class Messages(Base):
  __tablename__ = "messages"
  id = Column(
      UUID(as_uuid=True),
      primary_key=True,
      default=uuid.uuid4,
      nullable=False
  )

  # User relationship
  user_id = Column(
      UUID(as_uuid=True),
      ForeignKey('users.id', ondelete='CASCADE'),
      nullable=False
  )
  user = relationship("User", back_populates="messages")

  # Message details
  role = Column(
      Text,
      nullable=False,
      comment="Message role: 'user' or 'assistant'"
  )

  content = Column(
      Text,
      nullable=False,
      comment="Message content"
  )

  created_at = Column(
      TIMESTAMP(timezone=True),
      default=datetime.utcnow,
      nullable=False
  )

  # Metadata for additional context 
  message_metadata = Column(
      JSONB,
      nullable=True,
      comment="Additional message metadata"
  )

  def __repr__(self) -> str:
      return f"<ChatMessage(id={self.id}, role={self.role}, conversation_id={self.conversation_id})>"
