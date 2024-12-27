import requests

from ...models import GeneratedQuestions
from .llama_client import LlamaClient

llama_client = LlamaClient()


def check_llama_status():
    """Check if LLaMA API is running."""
    try:
        response = requests.get(llama_client.api_url)
        if response.status_code == 200:
            return {"status": "LLaMA is running"}
        else:
            raise Exception("LLaMA API is not responding correctly.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error connecting to LLaMA API: {e}")


def ask_llama_questions(employee_role: str):
    """Send a prompt to LLaMA API and return the generated response."""
    prompt = (
        f"Write 5 questions which you ask a manager about an employee who is a {employee_role}. The questions should "
        "be designed to gather enough detail to write a review. Questions need to be simple, short, and general. "
        "Avoid using any specific names, roles, or project titles. These questions will be shown to the manager. "
        "Write it in the JSON format. Don't add any additional text, output must be only in the JSON format. " 
        "JSON format must be strictly as follows: "
        "{questions: [\"[question text]\", \"[question text]\", \"[question text]\", \"[question text]\", "
        "\"[question text]\"] }. Note: Replace [question text] with the actual question text."
    )

    try:
        response = llama_client.call_model(prompt)
        return GeneratedQuestions.from_json(response)
    except Exception as e:
        raise Exception(f"Error generating questions from LLaMA API: {e}")
