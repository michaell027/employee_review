import json
from dataclasses import dataclass


@dataclass
class Message:
    role: str
    content: str

    @staticmethod
    def from_json(response: str | dict) -> "Message":
        """
        Creates an instance of Message from a JSON string or dictionary.
        """
        if isinstance(response, str):
            # Parse the JSON string into a dictionary
            response = json.loads(response)
        if not isinstance(response, dict) or "role" not in response or "content" not in response:
            raise ValueError("Invalid response format. Expected JSON with 'role' and 'content' fields.")
        return Message(role=response["role"], content=response["content"])