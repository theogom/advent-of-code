from day_abstract import DayAbstract


class Day2(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self):
        return [list(map(int, line.split("x"))) for line in self.data.split("\n")]

    def part_one(self) -> int:
        items = self.parse()
        paper = 0

        for item in items:
            l, w, h = item
            areas = [l * w, w * h, l * h]
            paper += sum(map(lambda x: 2 * x, areas)) + min(areas)

        return paper

    def part_two(self) -> int:
        items = self.parse()
        ribbon = 0

        for item in items:
            l, w, h = item
            perimeters = [2 * (l + w), 2 * (w + h), 2 * (l + h)]
            volume = l * w * h
            ribbon += min(perimeters) + volume

        return ribbon
