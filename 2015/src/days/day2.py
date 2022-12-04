from .day import DayAbstract


class Day(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self, data: str) -> list:
        return [list(map(int, line.split('x'))) for line in data.split('\n')]

    def part_one(self) -> int:
        paper = 0

        for item in self.data:
            l, w, h = item
            areas = [l * w, w * h, l * h]
            paper += sum(map(lambda x: 2 * x, areas)) + min(areas)

        return paper

    def part_two(self) -> int:
        ribbon = 0

        for item in self.data:
            l, w, h = item
            perimeters = [2 * (l + w), 2 * (w + h), 2 * (l + h)]
            volume = l * w * h
            ribbon += min(perimeters) + volume

        return ribbon
