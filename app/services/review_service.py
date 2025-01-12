from app.models import Evaluation
from app.services import make_answers_from_evaluation_neutral, generate_review_based_on_evaluation


def generate_review_from_evaluation(evaluation: Evaluation):
    neutral_evaluation = make_answers_from_evaluation_neutral(evaluation)
    review = generate_review_based_on_evaluation(neutral_evaluation)
    return review
