from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.adapters.repositories import SqlEmployeeRepository
from app.drivers import get_db
from app.use_cases import GetAllManagerEmployeesUseCase

router = APIRouter()


def get_all_manager_employees_use_case(
    employee_repository: SqlEmployeeRepository = Depends()
):
    return GetAllManagerEmployeesUseCase(employee_repository)


@router.get("/managers/{manager_id}/employees", tags=["employees"])
def get_managed_employees(
    manager_id: int,  # Manager ID as a path parameter
    db: Session = Depends(get_db),
    use_case: GetAllManagerEmployeesUseCase = Depends(get_all_manager_employees_use_case),
):
    """Get all employees who are managed by a specific manager."""
    try:
        return use_case.execute(db, manager_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
