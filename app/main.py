from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI Application",
    description="An example FastAPI application using Poetry for dependency management",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}
