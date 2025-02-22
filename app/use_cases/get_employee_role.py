from app.ports import EmployeeRepository
from sqlalchemy.orm import Session


class GetEmployeeRoleUseCase:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self, employee_id: int, db: Session) -> str:
        employee_role = self.employee_repository.get_role_by_id(db, employee_id)
        if employee_role is None:
            raise ValueError(f"Employee with ID {employee_id} not found.")
        return employee_role
