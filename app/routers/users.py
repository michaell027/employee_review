from fastapi import APIRouter

from app.crud import get_employee_role_by_id

router = APIRouter()


@router.get("/users/role", tags=["users"])
async def read_users(user_id: int):
    return get_employee_role_by_id(user_id)


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}
