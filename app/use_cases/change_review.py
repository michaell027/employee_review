from typing import List, Dict

from app.drivers.llama import ask_llama_to_change_review


class ChangeReviewUseCase:
    def execute(self, messages: List[Dict[str, str]]) -> List[Dict]:
        if messages is None:
            raise ValueError(f"Invalid messages: {messages}")
        generated_review = ask_llama_to_change_review(messages)
        return generated_review.replace("\n", " ").strip()