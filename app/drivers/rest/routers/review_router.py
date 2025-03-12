import asyncio
import json
from typing import List, Dict
from fastapi.responses import StreamingResponse
from fastapi import APIRouter, Depends, HTTPException
from app.domain.value_objects import Evaluation
from app.use_cases import GenerateReviewFromEvaluationUseCase, ChangeReviewUseCase

router = APIRouter()


def get_generate_review_from_evaluation_use_case(
):
    return GenerateReviewFromEvaluationUseCase()


def get_change_review_use_case(
):
    return ChangeReviewUseCase()


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


@router.post("/review/change", tags=["llama"])
async def chat(messages: List[Dict[str, str]], use_case: ChangeReviewUseCase = Depends(get_change_review_use_case)):
    """Handle chat messages with LLaMA API and stream responses."""
    try:
        response_stream = await use_case.execute(messages, stream=True)

        async def stream_generator():
            try:
                async for chunk in response_stream:
                    # Proper SSE format
                    yield f"data: {chunk}\n\n"
                    # Give the event loop a chance to send the data
                    await asyncio.sleep(0)
            except Exception as e:
                yield f"data: {{\"error\": \"{str(e)}\"}}\n\n"
                # End the stream properly
                yield "data: [DONE]\n\n"

        return StreamingResponse(
            stream_generator(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",  # Disable Nginx buffering
                "Access-Control-Allow-Origin": "*",  # CORS header
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


