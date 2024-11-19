from fastapi import APIRouter
from ai_services import generate_manager_questions

router = APIRouter()

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}

@router.get("/users/generate_questions", tags=["users"])
async def generate_questions():
    print("Generating questions...")
    result = generate_manager_questions()
    return result
