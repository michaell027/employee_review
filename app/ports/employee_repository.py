from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from app.domain.entities import Employee


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
