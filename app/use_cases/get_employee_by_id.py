from datetime import date
from typing import Any
from app.ports import EmployeeRepository
from sqlalchemy.orm import Session
from sqlalchemy import extract

from app.domain.entities import Review


class GetEmployeeByIdUseCase:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self, employee_id: int, db: Session) -> dict[str, Any | None]:
        employee = self.employee_repository.get_employee_by_id(db, employee_id)
        if employee is None:
            raise ValueError(f"Employee with ID {employee_id} not found.")

        current_year = date.today().year
        review = (
            db.query(Review)
            .filter(Review.employee_id == employee_id, extract("year", Review.created_at) == current_year)
            .first()
        )

        return {
            "id": employee.id,
            "name": employee.name,
            "email": employee.email,
            "position": employee.position,
            "department": employee.department.name if employee.department else None,
            "manager": employee.manager.name if employee.manager else None,
            "birthday": employee.birthday,
            "join_date": employee.join_date,
            "review": {
                "id": review.id,
                "content": review.review,
                "created_at": review.created_at
            } if review else None
        }
