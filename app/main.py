from fastapi import FastAPI
from app.routers import users_router, questions_router, review_router


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

app.include_router(users_router)
app.include_router(questions_router)
app.include_router(review_router)
