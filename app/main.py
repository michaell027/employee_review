from fastapi import FastAPI
from app.drivers.rest.routers import llama_router, questions_router, review_router, user_router
from app.adapters import global_exception_handler

app = FastAPI(
    title="Employee Review Generator",
    description=(
        "A FastAPI application designed to assist managers in creating structured employee reviews. "
        "The application leverages LLaMA-based AI to generate initial questions about an employee based on their "
        "position."
        "Managers provide answers to these questions, and the system generates a comprehensive review tailored to the "
        "input."
        "Built with Python  , it emphasizes ease of use and efficiency in performance review processes."
    ),
    version="1.0.0",
)

app.add_exception_handler(Exception, global_exception_handler)

app.include_router(user_router)
app.include_router(questions_router)
app.include_router(llama_router)
app.include_router(review_router)
