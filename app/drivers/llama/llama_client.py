import json

import requests

from app.domain.value_objects import LlamaResponse
from app.drivers.llama.llama_config import API_URL, HEADERS, MODEL_NAME
from app.domain.value_objects import LlamaChatResponse, Review


class LlamaClient:
    def __init__(self):
        """
        Initializes the Llama client with the specified model and configurations.
        """
        self.api_url = API_URL
        self.model = MODEL_NAME
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

    def call_chat_model(self, messages, json_format, stream=False):
        """
        Calls the chat Llama model with provided messages and settings.
        Args:
            messages (list): List of messages to send to the AI model.
            json_format (dict): Format of the response from the AI model.
            stream (bool): Stream the response from the AI model.
        Returns:
            str: Extracted 'review' field from the AI model response.
        """

        data = {
            "model": self.model,
            "messages": [
                            {
                                "content": "You are an AI assistant, which is helping me changing following review "
                                           "based on"
                                           "the user input.",
                                "role": "system",
                            },
                        ] + messages,
            "stream": stream,
            "format": json_format,
            "options": {"temperature": 0.5, "top_p": 0.9, "top_k": 75}
        }

        try:
            response = requests.post(f"{self.api_url}/api/chat", json=data, headers=self.headers)
            if response.status_code == 200:
                parsed_response = LlamaChatResponse(**response.json()).parsed_response

                try:
                    review_data = json.loads(parsed_response)
                except json.JSONDecodeError:
                    raise ValueError(f"Invalid JSON response from LLaMA API: {parsed_response}")

                return Review.from_json(review_data).review

            else:
                raise Exception(f"LLaMA API is not responding correctly. Status: {response.status_code}")

        except requests.exceptions.RequestException as e:
            raise Exception(f"Error connecting to LLaMA API: {e}")
