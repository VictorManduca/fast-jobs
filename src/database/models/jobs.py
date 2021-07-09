from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from src.database.models.base_model import Base

class Jobs(Base):
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)
  company = Column(String, nullable=False)
  location = Column(String, nullable=False)
  is_active = Column(Boolean(), default=True)
  owner_id = Column(Integer, ForeignKey("users.id"))
  owner = relationship("users", back_populates="jobs")
  description = Column(String)
  company_url = Column(String)
  date_posted = Column(Date)
