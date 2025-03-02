from app.ports import EmployeeRepository
from sqlalchemy.orm import Session


class GetAllManagerEmployeesUseCase:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self, db: Session, manager_id: int):
        employees = self.employee_repository.get_all_manager_employees(db, manager_id)
        if not employees:
            raise ValueError("No employees found.")

        return [
            {
                "id": employee.id,
                "name": employee.name,
                "email": employee.email,
                "position": employee.position,
                "department": employee.department.name if employee.department else None,
                "manager": employee.manager.name if employee.manager else None,
                "birthday": employee.birthday,
                "join_date": employee.join_date,
                "is_manager": employee.is_manager,
            } for employee in employees
        ]
