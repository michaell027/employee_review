from app.ports import EmployeeRepository
from typing import List, Dict
from sqlalchemy.orm import Session

from app.drivers.llama import ask_llama_questions


class GenerateEmployeeQuestionsUseCase:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self, employee_id: int, db: Session) -> List[Dict]:
        employee_role = self.employee_repository.get_role_by_id(db, employee_id)
        if employee_role is None:
            raise ValueError(f"Employee with ID {employee_id} not found.")
        generated_questions = ask_llama_questions(employee_role)
        return generated_questions.questions
