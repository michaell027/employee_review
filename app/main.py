import json

from fastapi import FastAPI, WebSocket
from app.drivers.rest.routers import llama_router, questions_router, review_router, user_router, manager_router, \
    employee_router
from app.adapters import global_exception_handler
from fastapi.middleware.cors import CORSMiddleware
from app.drivers.llama.llama_client import LlamaClient

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(Exception, global_exception_handler)

app.include_router(user_router)
app.include_router(questions_router)
app.include_router(llama_router)
app.include_router(review_router)
app.include_router(manager_router)
app.include_router(employee_router)

ollamaClient = LlamaClient()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        raw_text = await websocket.receive_text()

        print(f"Received message: {raw_text}")

        if not raw_text:
            await websocket.send_text("Please write something.")
            continue

        try:
            messages = json.loads(raw_text)

            if not isinstance(messages, list):
                await websocket.send_text("Invalid format. Expected a list of messages.")
                continue

            full_messages = [
                {
                    "role": "system",
                    "content": "You are an AI assistant, which is helping me change the following review based on the "
                               "user input."
                }
            ] + messages

            data_from_llama = ollamaClient.client.chat(
                model=ollamaClient.model,
                messages=full_messages,
                stream=True,
                options={
                    "temperature": 0.5,
                    "top_p": 0.9,
                    "top_k": 75
                },
                format={
                    "type": "object",
                    "properties": {
                        "review": {
                            "type": "string"
                        }
                    },
                    "required": ["review"]
                }
            )

            for chunk in data_from_llama:
                await websocket.send_text(chunk["message"]["content"])

        except json.JSONDecodeError:
            await websocket.send_text("Invalid JSON. Please send a valid list of messages.")