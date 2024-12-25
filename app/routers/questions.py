from fastapi import APIRouter, HTTPException

from app.services import check_llama_status, generate_questions_for_specific_employee

router = APIRouter()


@router.get("/llama/status", tags=["llama"])
def llama_status():
    """Check if LLaMA API is running."""
    try:
        return check_llama_status()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/llama/questions", tags=["llama"])
def llama_ask(employee_id: int):
    """Ask LLaMA to generate questions."""
    try:
        return generate_questions_for_specific_employee(employee_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
