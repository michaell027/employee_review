from app.models import Employee
from sqlalchemy.orm import Session


def get_employee_by_id(db: Session, employee_id: int) -> Employee:
    """Gets employee by ID."""
    return db.query(Employee).filter(Employee.id == employee_id).first()


def get_employee_role_by_id(employee_id: int, db: Session) -> str:
    """Gets employee role by ID."""
    employee = db.query(Employee.position).filter(Employee.id == employee_id).first()
    return employee.position if employee else None

