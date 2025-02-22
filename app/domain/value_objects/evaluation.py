import json
from dataclasses import dataclass


@dataclass
class QuestionsWithAnswers:
    question: str
    answer: str


@dataclass
class Evaluation:
    evaluation: list[QuestionsWithAnswers]

    @property
    def questions(self) -> list[str]:
        return [qa.question for qa in self.evaluation]

    @staticmethod
    def to_json(evaluation: "Evaluation") -> str:
        evaluation_list = []
        for qa in evaluation.evaluation:
            evaluation_list.append({"question": qa.question, "answer": qa.answer})
        return json.dumps({"evaluation": evaluation_list})

    @staticmethod
    def from_json(response: str | dict) -> "Evaluation":
        if isinstance(response, str):
            response = json.loads(response)
        if not isinstance(response, dict) or "evaluation" not in response:
            raise ValueError("Invalid response format. Expected JSON with an 'evaluation' field.")

        evaluation_data = response["evaluation"]
        if not isinstance(evaluation_data, list):
            raise ValueError("The 'evaluation' field must be a list.")

        evaluation: list[QuestionsWithAnswers] = []
        for qa_data in evaluation_data:
            if not isinstance(qa_data, dict) or "question" not in qa_data or "answer" not in qa_data:
                raise ValueError("Invalid format for a question/answer pair. Expected a dictionary with 'question' "
                                 "and 'answer' keys.")
            evaluation.append(QuestionsWithAnswers(question=qa_data["question"], answer=qa_data["answer"]))

        return Evaluation(evaluation=evaluation)
