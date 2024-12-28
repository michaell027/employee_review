from fastapi import APIRouter

from app.models import Evaluation

router = APIRouter()


@router.post("/review", tags=["review"])
async def generate_review(evaluation: Evaluation):
    return {"review": "fake review"}
