from dataclasses import dataclass, field
from typing import List, Optional


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

    @property
    def parsed_response(self) -> Optional[dict]:
        """Parses the response field if it's JSON."""
        import json
        try:
            return json.loads(self.response)
        except json.JSONDecodeError:
            return None
