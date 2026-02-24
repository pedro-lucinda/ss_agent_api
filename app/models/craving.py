from app.core.db.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Craving(Base):
  __tablename__ = "craving"
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey("users.id"))
  user = relationship("User", back_populates="craving")
  description = Column(String, nullable=False)
  intensity = Column(Integer, nullable=False)
  trigger = Column(String, nullable=False)
  smoked = Column(Boolean, nullable=False)
  total_smoked_cigarettes = Column(Integer, nullable=False)
  created_at = Column(DateTime, nullable=False)
  updated_at = Column(DateTime, nullable=False)
  date = Column(Date, nullable=False)