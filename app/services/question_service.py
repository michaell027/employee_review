from . import ask_llama_questions
from ..crud import get_employee_role_by_id


def generate_questions_for_specific_employee(employee_id: int):
    employee_role = get_employee_role_by_id(employee_id)
    if employee_role is None:
        raise ValueError(f"Employee with ID {employee_id} not found.")
    questions = ask_llama_questions(employee_role)
    return questions

