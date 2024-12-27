from dataclasses import dataclass
from typing import List


@dataclass
class QuestionsWithAnswers:
    question: str
    answer: str


@dataclass
class Evaluation:
    questions_with_answers: List[QuestionsWithAnswers]

    @property
    def questions(self) -> List[str]:
        return [qa.question for qa in self.questions_with_answers]
