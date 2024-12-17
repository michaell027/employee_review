import requests
import json
from .config import API_URL, MODEL_NAME, HEADERS


class LlamaClient:
    def __init__(self):
        """
        Initializes the Llama client with the specified model and configurations.
        """
        self.api_url = API_URL
        self.model = MODEL_NAME
        self.headers = HEADERS

    def call_model(self, prompt, stream=False):
        """
        Calls the Llama model with provided messages and settings.
        Args:
            prompt (str): Prompt to send to the AI model.
            stream (bool): Stream the response from the AI model.
        Returns:
            dict: Response from the AI model.
        """
        data = {
            "prompt": prompt,
            "stream": stream,
            "model": self.model
        }

        try:
            response = requests.post(f"{self.api_url}/api/generate", data=json.dumps(data), headers=self.headers)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception("LLaMA API is not responding correctly.")

        except requests.exceptions.RequestException as e:
            raise Exception(f"Error connecting to LLaMA API: {e}")
