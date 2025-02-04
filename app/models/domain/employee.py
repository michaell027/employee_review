from sqlalchemy import Column, Integer, String
from app.utils import Base


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    position = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"Employee(id={self.id}, name={self.name}, email={self.email}, position={self.position}, age={self.age})"
