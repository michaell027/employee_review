from datetime import date
from typing import Dict, Any

from sqlalchemy import Column

from app.ports import EmployeeRepository
from sqlalchemy.orm import Session


class GetEmployeeByIdUseCase:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self, employee_id: int, db: Session) -> dict[str, Any | None]:
        employee = self.employee_repository.get_employee_by_id(db, employee_id)
        if employee is None:
            raise ValueError(f"Employee with ID {employee_id} not found.")
        return {
            "id": employee.id,
            "name": employee.name,
            "email": employee.email,
            "position": employee.position,
            "department": employee.department.name if employee.department else None,
            "manager": employee.manager.name if employee.manager else None,
            "birthday": employee.birthday,
            "join_date": employee.join_date
        }
