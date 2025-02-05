from fastapi import APIRouter

from app.crud import get_employee_role_by_id
from app.utils import get_db
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/users/role", tags=["users"])
async def read_users(user_id: int, db: Session = Depends(get_db)):
    return get_employee_role_by_id(user_id, db)


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}
