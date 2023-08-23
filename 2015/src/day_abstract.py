from abc import ABC, abstractmethod
from typing import Any


class DayAbstract(ABC):
    def __init__(self, data: str) -> None:
        self.data = data

    def parse(self) -> Any:
        return self.data

    @abstractmethod
    def part_one(self) -> int:
        pass

    @abstractmethod
    def part_two(self) -> int:
        pass
