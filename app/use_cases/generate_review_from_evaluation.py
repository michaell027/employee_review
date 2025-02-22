from typing import List, Dict
from app.domain.value_objects import Evaluation
from app.services import make_answers_from_evaluation_neutral, generate_review_based_on_evaluation


class GenerateReviewFromEvaluationUseCase:
    def execute(self, evaluation: Evaluation) -> List[Dict]:
        neutral_evaluation = make_answers_from_evaluation_neutral(evaluation)
        review = generate_review_based_on_evaluation(neutral_evaluation)
        if review is None:
            raise ValueError(f"Review not generated.")
        return review
