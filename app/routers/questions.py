from fastapi import APIRouter, HTTPException

from app.services import check_llama_status, ask_llama_questions

router = APIRouter()


@router.get("/llama/status", tags=["llama"])
def llama_status():
    """Check if LLaMA API is running."""
    try:
        return check_llama_status()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/llama/questions", tags=["llama"])
def llama_ask():
    """Ask LLaMA to generate questions."""
    try:
        return ask_llama_questions()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
