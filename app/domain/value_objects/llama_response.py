from dataclasses import dataclass, field
from typing import List, Optional
import json
from ollama import GenerateResponse


@dataclass
class LlamaResponse:
    model: str
    created_at: str
    response: str
    done: bool
    done_reason: str
    context: List[int]
    total_duration: int
    load_duration: int
    prompt_eval_count: int
    prompt_eval_duration: int
    eval_count: int
    eval_duration: int

    parsed_response: Optional[dict] = field(default=None, init=False)

    def __post_init__(self):
        """Post-initialization to parse the JSON response."""
        try:
            self.parsed_response = json.loads(self.response)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON response: {e}")
        except TypeError as e:
            raise ValueError(f"Invalid response type: {e}")
        except Exception as e:
            raise ValueError(f"Unexpected error during JSON parsing: {e}")

    @classmethod
    def from_json(cls, data: GenerateResponse) -> 'LlamaResponse':
        """Creates an instance of LlamaResponse from a JSON-like object."""
        return cls(
            model=data.model,
            created_at=data.created_at,
            response=data.response,
            done=data.done,
            done_reason=data.done_reason,
            context=data.context,
            total_duration=data.total_duration,
            load_duration=data.load_duration,
            prompt_eval_count=data.prompt_eval_count,
            prompt_eval_duration=data.prompt_eval_duration,
            eval_count=data.eval_count,
            eval_duration=data.eval_duration
        )
