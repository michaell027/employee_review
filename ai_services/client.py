import torch
from transformers import pipeline

class AIClient:
    def __init__(self, model_id="meta-llama/Llama-3.2-3B-Instruct"):
        """
        Initializes the AI client with the specified model and configurations.
        """
        print("Initializing AI client...")
        self.pipe = pipeline(
            "text-generation",
            model=model_id,
            torch_dtype=torch.bfloat16,
            device_map="auto"
        )

    def call_model(self, messages, max_new_tokens=256):
        """
        Calls the AI model with provided messages and settings.
        Args:
            messages (list): List of messages to pass to the model.
            max_new_tokens (int): Maximum number of tokens for the response.
        Returns:
            dict: Response from the AI model.
        """
        return self.pipe(messages, max_new_tokens=max_new_tokens)
