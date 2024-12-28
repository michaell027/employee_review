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
