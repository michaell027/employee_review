from typing import Type

from app.ports import EmployeeRepository
from app.domain.entities import Employee
from sqlalchemy.orm import Session


class SqlEmployeeRepository(EmployeeRepository):
    """Implementation of the EmployeeRepository using SQLAlchemy."""

    def get_by_id(self, db: Session, employee_id: int) -> Type[Employee] | None:
        """Gets employee by ID."""
        return db.query(Employee).filter(Employee.id == employee_id).first()

    def get_role_by_id(self, db: Session, employee_id: int) -> str:
        """Gets employee role by ID."""
        employee = db.query(Employee.position).filter(Employee.id == employee_id).first()
        return employee.position if employee else None

    def get_all_users(self, db: Session) -> list[Type[Employee]]:
        """Gets all employees."""
        return db.query(Employee).all()
