from app.ports import EmployeeRepository
from sqlalchemy.orm import Session
from datetime import datetime

from app.domain.entities import Employee, Review


# TODO: Rename to employees

class GetAllUsersUseCase:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self, db: Session):
        users = self.employee_repository.get_all_users(db)
        if not users:
            raise ValueError("No users found.")

        current_year = datetime.now().year

        return [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "position": user.position,
                "department": user.department.name if user.department else None,
                "manager": user.manager.name if user.manager else None,
                "birthday": user.birthday,
                "join_date": user.join_date,
                "is_manager": user.is_manager,
                "is_review_generated": db.query(Review)
                                       .filter(Review.employee_id == user.id)
                                       .filter(Review.created_at >= datetime(current_year, 1, 1))
                                       .filter(Review.created_at < datetime(current_year + 1, 1, 1))
                                       .first() is not None
            }
            for user in users
        ]
