from app.ports import EmployeeRepository
from sqlalchemy.orm import Session

from app.domain.entities import Employee


class GetAllUsersUseCase:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self, db: Session):
        users = self.employee_repository.get_all_users(db)
        if not users:
            raise ValueError("No users found.")

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
            }
            for user in users
        ]