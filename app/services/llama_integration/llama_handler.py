import requests
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


def ask_llama_questions():
    """Send a prompt to LLaMA API and return the generated response."""
    prompt = ("Write 5 questions which you ask manager about the employee who is web developer. The questions should "
              "be designed to gather enough detail to write a review. Questions need to be simple and short. No "
              "additional information. These questions will be shown to manager. Write it in the json format: {"
              "questions:[...]}, no additional text.")
    try:
        response = llama_client.call_model(prompt)
        return response
    except Exception as e:
        raise Exception(f"Error generating questions from LLaMA API: {e}")
