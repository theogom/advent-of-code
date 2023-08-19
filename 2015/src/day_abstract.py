from abc import ABC, abstractmethod


class DayAbstract(ABC):
    def __init__(self, data: str) -> None:
        self.data = data

    def parse(self) -> str:
        return self.data

    @abstractmethod
    def part_one(self) -> int:
        pass

    @abstractmethod
    def part_two(self) -> int:
        pass
