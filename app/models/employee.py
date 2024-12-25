from dataclasses import dataclass


@dataclass
class Employee:
    id: int
    name: str
    email: str
    position: str
    age: int


