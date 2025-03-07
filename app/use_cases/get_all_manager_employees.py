from app.ports import EmployeeRepository
from sqlalchemy.orm import Session
from datetime import datetime

from app.domain.entities import Review


class GetAllManagerEmployeesUseCase:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self, db: Session, manager_id: int):
        employees = self.employee_repository.get_all_manager_employees(db, manager_id)
        if not employees:
            raise ValueError("No employees found.")

        current_year = datetime.now().year

        return [
            {
                "id": employee.id,
                "name": employee.name,
                "position": employee.position,
                "department": employee.department.name if employee.department else None,
                "manager": employee.manager.name if employee.manager else None,
                "is_manager": employee.is_manager,
                "is_review_generated": db.query(Review)
                                       .filter(Review.employee_id == employee.id)
                                       .filter(Review.created_at >= datetime(current_year, 1, 1))
                                       .filter(Review.created_at < datetime(current_year + 1, 1, 1))
                                       .first() is not None
            } for employee in employees
        ]
