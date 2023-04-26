from typing import Optional

class Student:
    def __init__(self, name: str, grades: Optional[list[int]] = None) -> None:
        self.name = name
        self.grades = grades or []