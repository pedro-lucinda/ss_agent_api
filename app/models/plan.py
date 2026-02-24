from app.core.db.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum


class PlanType(PyEnum):
    gradual_cessation = "gradual_cessation"
    cold_turkey = "cold_turkey"

class Plan(Base):
  __tablename__ = "plans"
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey("users.id"))
  user = relationship("User", back_populates="plan")
  name = Column(String, nullable=False)
  description = Column(String, nullable=False)
  quit_date = Column(Date, nullable=False)
  created_at = Column(DateTime, nullable=False)
  updated_at = Column(DateTime, nullable=False)
  type = Column(Enum(PlanType), nullable=False)
  # if gradual cessation, the number of weeks to quit smoking
  weeks = Column(Integer, nullable=True)
  start_date = Column(Date, nullable=True)
  end_date = Column(Date, nullable=True)