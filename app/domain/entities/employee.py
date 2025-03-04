from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from app.drivers import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    position = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id", ondelete="SET NULL"))
    manager_id = Column(Integer, ForeignKey("employees.id", ondelete="SET NULL"))
    birthday = Column(Date)
    join_date = Column(Date)
    is_manager = Column(Boolean, default=False)

    department = relationship("Department", back_populates="employees")
    manager = relationship("Employee", remote_side=[id], backref="subordinates")

    def __repr__(self):
        return f"Employee(id={self.id}, name={self.name}, email={self.email}, position={self.position}, is_manager={self.is_manager})"
