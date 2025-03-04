from typing import Type

from app.ports import EmployeeRepository
from app.domain.entities import Employee
from sqlalchemy.orm import Session, joinedload


class SqlEmployeeRepository(EmployeeRepository):
    """Implementation of the EmployeeRepository using SQLAlchemy."""

    def get_by_id(self, db: Session, employee_id: int) -> Type[Employee] | None:
        """Gets employee by ID."""
        return db.query(Employee).filter(Employee.id == employee_id).first()

    def get_role_by_id(self, db: Session, employee_id: int) -> str:
        """Gets employee role by ID."""
        employee = db.query(Employee.position).filter(Employee.id == employee_id).first()
        return employee.position if employee else None

    def get_all_users(self, db: Session):
        """Gets all employees with department and manager names."""
        return (
            db.query(Employee)
            .options(
                joinedload(Employee.department),
                joinedload(Employee.manager)
            )
            .all()
        )

    def get_all_managers(self, db: Session):
        """Gets only employees who are managers (i.e., who have subordinates)."""
        return (
            db.query(Employee)
            .filter(Employee.is_manager == True)
            .options(
                joinedload(Employee.department),
                joinedload(Employee.subordinates)
            )
            .all()
        )

    def get_all_manager_employees(self, db: Session, manager_id: int):
        """Gets all employees who report to a given manager."""
        # TODO: Check if is manager
        return (
            db.query(Employee)
            .filter(Employee.manager_id == manager_id)
            .options(
                joinedload(Employee.department),
                joinedload(Employee.manager)
            )
            .all()
        )

    def get_employee_by_id(self, db: Session, employee_id: int):
        """Gets employee by ID."""
        return (db.query(Employee).filter(Employee.id == employee_id)
                .options(
            joinedload(Employee.department),
            joinedload(Employee.manager)
        ).first())
