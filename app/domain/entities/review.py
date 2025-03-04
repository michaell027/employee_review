from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.drivers import Base
from app.domain.entities.employee import Employee


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False)
    manager_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False)
    review = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    employee = relationship("Employee", foreign_keys=[employee_id])
    manager = relationship("Employee", foreign_keys=[manager_id])

    def __repr__(self):
        return f"Review(id={self.id}, employee_id={self.employee_id}, manager_id={self.manager_id}, created_at={self.created_at})"
