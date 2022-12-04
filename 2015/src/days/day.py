from abc import ABC, abstractmethod
from typing import Any


class DayAbstract(ABC):
    def __init__(self, data: str) -> None:
        self.data = self.parse(data)

    @abstractmethod
    def parse(self, data: str) -> Any:
        pass

    @abstractmethod
    def part_one(self) -> int:
        pass
    
    @abstractmethod
    def part_two(self) -> int:
        pass
