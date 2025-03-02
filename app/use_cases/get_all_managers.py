from app.ports import EmployeeRepository
from sqlalchemy.orm import Session


class GetAllManagersUseCase:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self, db: Session):
        managers = self.employee_repository.get_all_managers(db)
        if not managers:
            raise ValueError("No managers found.")

        return [
            {
                "id": manager.id,
                "name": manager.name,
                "position": manager.position,
            }
            for manager in managers
        ]
