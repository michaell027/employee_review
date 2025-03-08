from dataclasses import dataclass, field
from typing import Dict


@dataclass
class MessageModel:
    role: str
    content: str


@dataclass
class LlamaChatResponse:
    model: str
    created_at: str
    message: MessageModel
    done_reason: str
    done: bool
    total_duration: int
    load_duration: int
    prompt_eval_count: int
    prompt_eval_duration: int
    eval_count: int
    eval_duration: int

    def __post_init__(self):
        """Converts the message field to a MessageModel instance if it's a dictionary."""
        if isinstance(self.message, dict):
            self.message = MessageModel(**self.message)

    @property
    def parsed_response(self) -> str:
        """Returns the content of the message field."""
        return self.message.content
