from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.adapters.repositories import SqlEmployeeRepository
from app.use_cases import GenerateEmployeeQuestionsUseCase

from app.drivers import get_db

router = APIRouter()


def get_generate_employee_questions_use_case(
    employee_repository: SqlEmployeeRepository = Depends()
):
    return GenerateEmployeeQuestionsUseCase(employee_repository)


@router.get("/questions", tags=["llama"])
def llama_ask(
    employee_id: int,
    db: Session = Depends(get_db),
    use_case: GenerateEmployeeQuestionsUseCase = Depends(get_generate_employee_questions_use_case)
):
    """Ask LLaMA to generate questions."""
    try:
        return use_case.execute(employee_id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))