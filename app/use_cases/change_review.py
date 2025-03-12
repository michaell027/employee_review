from typing import List, Dict

from app.drivers.llama import ask_llama_to_change_review


class ChangeReviewUseCase:
    async def execute(self, messages: List[Dict[str, str]], stream=False):
        if messages is None:
            raise ValueError(f"Invalid messages: {messages}")

        try:
            # Call LLaMA API with streaming option
            result = await ask_llama_to_change_review(messages, stream)
            return result
        except Exception as e:
            # Re-raise to be handled by the router
            raise e

