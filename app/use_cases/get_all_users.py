from app.ports import EmployeeRepository
from sqlalchemy.orm import Session

from app.domain.entities import Employee


class GetAllUsersUseCase:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self, db: Session) -> list[Employee]:
        users = self.employee_repository.get_all_users(db)
        if not users:
            raise ValueError("No users found.")
        return users
