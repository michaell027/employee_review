from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from app.domain.entities import Employee, Review


class EmployeeRepository(ABC):
    @abstractmethod
    def get_by_id(self, db: Session, employee_id: int) -> Employee:
        pass

    @abstractmethod
    def get_role_by_id(self, db: Session, employee_id: int) -> str:
        pass

    @abstractmethod
    def get_all_users(self, db: Session) -> list[Employee]:
        pass

    @abstractmethod
    def get_all_managers(self, db: Session) -> list[Employee]:
        pass

    @abstractmethod
    def get_all_manager_employees(self, db: Session, manager_id: int) -> list[Employee]:
        pass

    @abstractmethod
    def get_employee_by_id(self, db: Session, employee_id: int) -> Employee:
        pass

    @abstractmethod
    def save_employee_review(self, db: Session, employee_id: int, manager_id: int, review_text: str) -> Review:
        pass
