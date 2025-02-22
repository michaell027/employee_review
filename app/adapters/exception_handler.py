from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger("uvicorn.error")


async def global_exception_handler(_: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error. Please contact support."},
    )
