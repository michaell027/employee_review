import requests
import json

from ...models import LlamaResponse
from .llama_config import API_URL, HEADERS


class LlamaClient:
    def __init__(self):
        """
        Initializes the Llama client with the specified model and configurations.
        """
        self.api_url = API_URL
        self.model = "llama3.2"
        self.headers = HEADERS

    def call_model(self, prompt, json_format, stream=False):
        """
        Calls the Llama model with provided messages and settings.
        Args:
            prompt (str): Prompt to send to the AI model.
            json_format (dict): Format of the response from the AI model.
            stream (bool): Stream the response from the AI model.
        Returns:
            str: Response from the AI model.
        """
        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream,
            "format": json_format,
            "options": {"temperature": 0.5, "top_p": 0.9, "top_k": 75}
        }

        try:
            response = requests.post(f"{self.api_url}/api/generate", json=data, headers=self.headers)
            print(response.json())
            if response.status_code == 200:
                return LlamaResponse(**response.json()).response
            else:
                raise Exception(f"LLaMA API is not responding correctly. Status: {response.status_code}")

        except requests.exceptions.RequestException as e:
            raise Exception(f"Error connecting to LLaMA API: {e}")
