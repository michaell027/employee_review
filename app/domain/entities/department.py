from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.drivers import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    employees = relationship("Employee", back_populates="department")

    def __repr__(self):
        return f"Department(id={self.id}, name={self.name})"
