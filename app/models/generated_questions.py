from dataclasses import dataclass
from typing import List, Union, Optional
import json


@dataclass
class GeneratedQuestions:
    questions: List[str]

    @staticmethod
    def from_json(response: Union[str, dict]) -> "GeneratedQuestions":
        """
        Creates an instance of GeneratedQuestions from a JSON string or dictionary.
        """
        if isinstance(response, str):
            try:
                response_dict = json.loads(response)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON string provided.")
        elif isinstance(response, dict):
            response_dict = response
        else:
            raise ValueError("Response must be a JSON string or dictionary.")

        questions_list = response_dict.get("questions", [])
        if not isinstance(questions_list, list) or not all(isinstance(q, str) for q in questions_list):
            raise ValueError("The 'questions' field must be a list of strings.")

        return GeneratedQuestions(questions=questions_list)

    @property
    def parsed_responses(self) -> List[Optional[Union[dict, list]]]:
        """Parses each string in the questions list as JSON, returning a list of parsed objects."""
        parsed = []
        for question in self.questions:
            try:
                parsed.append(json.loads(question))
            except json.JSONDecodeError:
                parsed.append(None)
        return parsed
