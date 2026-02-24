from app.core.db.base import Base
from sqlalchemy import Column, Integer, String, UUID, TIMESTAMP
import uuid
from datetime import datetime
from sqlalchemy.orm import relationship

class User(Base):
  __tablename__ = "users"
  
  id = Column(
          UUID(as_uuid=True),
          primary_key=True,
          default=uuid.uuid4,
          nullable=False
      )

      # Timestamps
  created_at = Column(
        TIMESTAMP(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
  updated_at = Column(
        TIMESTAMP(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Audit fields
  created_by = Column(UUID(as_uuid=True), nullable=True)
  updated_by = Column(UUID(as_uuid=True), nullable=True)

    # Auth0 integration
  auth0_id = Column(String, unique=True, nullable=False, index=True)
  email = Column(String, unique=True, nullable=False, index=True)

  # Basic profile information
  name = Column(String, nullable=False)
  age = Column(Integer, nullable=False)

  thread_id = Column(UUID(as_uuid=True), nullable=False)

  messages = relationship("ChatMessage", back_populates="user")

  diary_entries = relationship("DiaryEntry", back_populates="user")

  cravings = relationship("Cravings", back_populates="user")

  plan=relationship("Plan", back_populates="user")