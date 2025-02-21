from fastapi import APIRouter, HTTPException

from app.models import Evaluation
from app.services import generate_review_from_evaluation

router = APIRouter()


@router.post("/review", tags=["review"])
async def generate_review(evaluation: Evaluation):
    """Generate a review based on the evaluation."""
    try:
        return generate_review_from_evaluation(evaluation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
