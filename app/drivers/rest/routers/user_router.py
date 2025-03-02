from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.adapters.repositories import SqlEmployeeRepository
from app.use_cases import GetEmployeeRoleUseCase, GetAllUsersUseCase
from app.drivers import get_db

router = APIRouter()

# TODO: Get rid of it


def get_employee_role_use_case(
        employee_repository: SqlEmployeeRepository = Depends()
):
    return GetEmployeeRoleUseCase(employee_repository)


def get_all_users_use_case(
        employee_repository: SqlEmployeeRepository = Depends()
):
    return GetAllUsersUseCase(employee_repository)


@router.get("/users/me", tags=["users"])
def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/role", tags=["users"])
def read_users(
        user_id: int,
        db: Session = Depends(get_db),
        use_case: GetEmployeeRoleUseCase = Depends(get_employee_role_use_case)
):
    """Read user role."""
    try:
        return use_case.execute(user_id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/users", tags=["users"])
def read_users(
        db: Session = Depends(get_db),
        use_case: GetAllUsersUseCase = Depends(get_all_users_use_case)
):
    """Read all users."""
    try:
        return use_case.execute(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
