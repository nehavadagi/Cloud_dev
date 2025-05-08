from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base  # make sure Base is defined in db.py

class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    task_type = Column(String, nullable=False)
    input_data = Column(Text, nullable=False)
    output = Column(Text, nullable=True)
    status = Column(String, nullable=False, default="queued")

    user = relationship("User", back_populates="jobs")
