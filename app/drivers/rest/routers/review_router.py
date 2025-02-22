from fastapi import APIRouter, Depends, HTTPException
from app.domain.value_objects import Evaluation
from app.use_cases import GenerateReviewFromEvaluationUseCase

router = APIRouter()


def get_generate_review_from_evaluation_use_case(
):
    return GenerateReviewFromEvaluationUseCase()


@router.post("/review", tags=["review"])
def generate_review(
    evaluation: Evaluation,
    use_case: GenerateReviewFromEvaluationUseCase = Depends(get_generate_review_from_evaluation_use_case)
):
    """Generate a review based on the evaluation."""
    try:
        return use_case.execute(evaluation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))