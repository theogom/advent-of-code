from .day import DayAbstract


class Day(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self, data: str):
        return data

    def part_one(self) -> int:
        raise NotImplementedError

    def part_two(self) -> int:
        raise NotImplementedError
