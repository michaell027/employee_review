from app.utils import SessionLocal
from models.domain.employee import Employee


def get_employee_by_id(db: SessionLocal, employee_id: int) -> Employee:
    """Gets employee by ID."""
    return db.query(Employee).filter(Employee.id == employee_id).first()


def get_employee_role_by_id(db: SessionLocal, employee_id: int) -> str:
    """Gets employee role by ID."""
    employee = db.query(Employee.position).filter(Employee.id == employee_id).first()
    return employee.position if employee else None
