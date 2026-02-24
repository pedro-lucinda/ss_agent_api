

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Date,
)
from sqlalchemy.orm import relationship
from app.core.db.base import Base


class DiaryEntry(Base):
  __tablename__ = "diary_entries"
  
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey("users.id"))
  user = relationship("User", back_populates="diary_entries")
  content = Column(String, nullable=False)
  created_at = Column(DateTime, nullable=False)
  updated_at = Column(DateTime, nullable=False)
  mood_score = Column(Integer, nullable=False)
  total_smoked_cigarettes = Column(Integer, nullable=False)
  date = Column(Date, nullable=False)