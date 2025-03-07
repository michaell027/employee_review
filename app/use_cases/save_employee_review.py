from app.ports import EmployeeRepository
from sqlalchemy.orm import Session


class SaveEmployeeReviewUseCase:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self, db: Session, employee_id: int, manager_id: int, review_text: str) -> dict:
        """
        Saves a review to the database.

        :param db: Database session
        :param employee_id: ID of the employee being reviewed
        :param manager_id: ID of the manager providing
        :param review_text: The review text
        :return: The saved Review object
        """
        review = self.employee_repository.save_employee_review(db, employee_id, manager_id, review_text)
        return {
            "review": review.review,
            "created_at": review.created_at,
        }
