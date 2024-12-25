import json
from typing import Optional

from ..models import Employee


def get_employee_role_by_id(employee_id: int) -> Optional[str]:
    """
    Retrieve the position (role) of an employee by their ID from a JSON file.
    """

    file_path = "employees_data.json"
    try:
        with open(file_path, "r") as file:
            data = json.load(file)

        for employee in data.get("employees", []):
            if employee["id"] == employee_id:
                employee = Employee(
                    id=employee["id"],
                    name=employee["name"],
                    email=employee["email"],
                    position=employee["position"],
                    age=employee["age"]
                )
                return employee.position
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in file: {file_path}")

    return None
