import json
import requests

LLAMA_API_URL = "http://localhost:11434"
HEADERS = {
    "Content-Type": "application/json"
}


def check_llama_status():
    """Check if LLaMA API is running."""
    try:
        response = requests.get(f"{LLAMA_API_URL}")
        if response.status_code == 200:
            return {"status": "LLaMA is running"}
        else:
            raise Exception("LLaMA API is not responding correctly.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error connecting to LLaMA API: {e}")


def ask_llama_questions(prompt: str):
    """Send a prompt to LLaMA API and return the generated response."""
    try:
        data = {
            "prompt": prompt,
            "stream": False,
            "model": "llama3"
        }
        response = requests.post(f"{LLAMA_API_URL}/api/generate", data=json.dumps(data), headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("LLaMA API is not responding correctly.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error connecting to LLaMA API: {e}")
