from dataclasses import dataclass

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.adapters.repositories import SqlEmployeeRepository
from app.drivers import get_db
from app.use_cases import GetAllManagerEmployeesUseCase, GetEmployeeByIdUseCase, SaveEmployeeReviewUseCase

router = APIRouter()


def get_all_manager_employees_use_case(
        employee_repository: SqlEmployeeRepository = Depends()
):
    return GetAllManagerEmployeesUseCase(employee_repository)


def get_employee_by_id_use_case(
        employee_repository: SqlEmployeeRepository = Depends()
):
    return GetEmployeeByIdUseCase(employee_repository)


def save_employee_review_use_case(
        employee_repository: SqlEmployeeRepository = Depends()
):
    return SaveEmployeeReviewUseCase(employee_repository)


@router.get("/managers/{manager_id}/employees", tags=["employees"])
def get_managed_employees(
        manager_id: int,
        db: Session = Depends(get_db),
        use_case: GetAllManagerEmployeesUseCase = Depends(get_all_manager_employees_use_case),
):
    """Get all employees who are managed by a specific manager."""
    try:
        return use_case.execute(db, manager_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/employees/{employee_id}", tags=["employees"])
def get_employee_by_id(
        employee_id: int,
        db: Session = Depends(get_db),
        use_case: GetEmployeeByIdUseCase = Depends(get_employee_by_id_use_case),
):
    """Get employee by ID."""
    try:
        return use_case.execute(employee_id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@dataclass
class ReviewRequest:
    review: str
    managerId: int


@router.post("/employees/{employee_id}/review", tags=["employees"])
def generate_review(
        employee_id: int,
        review_data: ReviewRequest,
        db: Session = Depends(get_db),
        use_case: SaveEmployeeReviewUseCase = Depends(save_employee_review_use_case),
):
    """Generate a review for an employee."""
    try:
        return use_case.execute(db, employee_id, review_data.managerId, review_data.review)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
