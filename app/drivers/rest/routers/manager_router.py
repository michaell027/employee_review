from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.adapters.repositories import SqlEmployeeRepository
from app.drivers import get_db
from app.use_cases import GetAllManagersUseCase

router = APIRouter()


def get_all_managers_use_case(
        employee_repository: SqlEmployeeRepository = Depends()
):
    return GetAllManagersUseCase(employee_repository)


@router.get("/managers", tags=["managers"])
def get_managers(
        db: Session = Depends(get_db),
        use_case: GetAllManagersUseCase = Depends(get_all_managers_use_case)
):
    """Get all employees who are managers."""
    try:
        return use_case.execute(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
