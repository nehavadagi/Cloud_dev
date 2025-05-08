from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String)
    result = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="history")
