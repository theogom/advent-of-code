from .day import DayAbstract


class Day(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self, data) -> str:
        return data

    def part_one(self) -> int:
        floor = 0
        
        for char in self.data:
            floor += 1 if char == '(' else -1
        
        return floor

    def part_two(self) -> int:
        floor = 0

        for index, char in enumerate(self.data):
            floor += 1 if char == '(' else -1

            if floor < 0:
                return index + 1
        
        return 0
