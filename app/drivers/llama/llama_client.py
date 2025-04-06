from ollama import Client
import requests

from app.domain.value_objects import LlamaResponse
from app.drivers.llama.llama_config import API_URL, MODEL_NAME


class LlamaClient:
    def __init__(self):
        """
        Initializes the Llama client with the specified model and configurations.
        """
        self.model = MODEL_NAME
        self.client = Client(host=API_URL)

    def call_model(self, prompt, json_format, stream=False):
        try:
            response = self.client.generate(
                model=self.model,
                prompt=prompt,
                format=json_format,
                options={
                    "temperature": 0.5,
                    "top_p": 0.9,
                    "top_k": 75
                },
            )

            if isinstance(response, str):
                response = response.strip()

            parsed_response = LlamaResponse.from_json(response)

            if parsed_response is None:
                raise ValueError("Parsed response is None. Check the response format.")

            if not parsed_response.response:
                raise ValueError("Parsed response is empty. Check the response format.")

            return parsed_response.response

        except requests.exceptions.RequestException as e:
            raise Exception(f"Error connecting to LLaMA API: {e}")
        except ValueError as e:
            print(f"Error parsing response: {e}")
            raise

    # TODO: Remove this function
    def call_chat_model(self, messages):
        """
        Calls the chat Llama model with provided messages and settings.
        Args:
            messages (list): List of messages to send to the AI model.
        Returns:
            str: Extracted 'review' field from the AI model response.
        """

        full_messages = [
                            {
                                "role": "system",
                                "content": "You are an AI assistant, which is helping me change the following review "
                                           "based on"
                                           "the user input."
                            }
                        ] + messages

        try:
            response = self.client.chat(
                model=self.model,
                messages=full_messages,
                stream=True
            )

            return response

        except Exception as e:
            raise Exception(f"Error connecting to LLaMA API: {e}")
