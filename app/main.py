from fastapi import FastAPI
from .routers import users_router
app = FastAPI(
    title="My FastAPI Application",
    description="An example FastAPI application using Poetry for dependency management",
    version="1.0.0",
)

app.include_router(users_router)
