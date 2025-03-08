import json
from dataclasses import dataclass


@dataclass
class Review:
    review: str

    @staticmethod
    def from_json(response: str | dict) -> "Review":
        """
        Creates an instance of Review from a JSON string or dictionary.
        """
        if isinstance(response, str):
            # Parse the JSON string into a dictionary
            response = json.loads(response)
        if not isinstance(response, dict) or "review" not in response:
            raise ValueError("Invalid response format. Expected JSON with a 'review' field.")
        return Review(review=response["review"])
