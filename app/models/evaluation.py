import json
from dataclasses import dataclass
from typing import List


@dataclass
class QuestionsWithAnswers:
    question: str
    answer: str


@dataclass
class Evaluation:
    evaluation: List[QuestionsWithAnswers]

    @property
    def questions(self) -> List[str]:
        return [qa.question for qa in self.evaluation]

    @staticmethod
    def to_json(evaluation: "Evaluation") -> str:
        """
        Converts an instance of Evaluation to a JSON string.
        """
        return json.dumps(
            {"evaluation": [
                {"question": qa.question, "answer": qa.answer}
                for qa in evaluation.evaluation
            ]})

    @staticmethod
    def from_json(response: str | dict) -> "Evaluation":
        """
        Creates an instance of Evaluation from a JSON string or dictionary.
        """
        if isinstance(response, str):
            response = json.loads(response)
        if not isinstance(response, dict) or "evaluation" not in response:
            raise ValueError("Invalid response format. Expected JSON with an 'evaluation' field.")
        evaluation = response["evaluation"]
        if not isinstance(evaluation, list):
            raise ValueError("The 'evaluation' field must be a list.")
        return Evaluation(evaluation=[
            QuestionsWithAnswers(question=qa["question"], answer=qa["answer"])
            for qa in evaluation
        ])
