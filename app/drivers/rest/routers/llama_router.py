from fastapi import APIRouter, HTTPException

from app.drivers.llama import check_llama_status

router = APIRouter()


@router.get("/llama/status", tags=["llama"])
def llama_status():
    """Check if LLaMA API is running."""
    try:
        return check_llama_status()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))