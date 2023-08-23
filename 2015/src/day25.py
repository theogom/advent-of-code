import re
from functools import reduce

from day_abstract import DayAbstract


class Day25(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self):
        # Zero-based index
        return map(lambda x: int(x) - 1, re.findall(r"\d+", self.data))

    def part_one(self):
        row, column = self.parse()
        code_index = get_code_index(row, column)
        return get_code(code_index)

    def part_two(self):
        pass


def get_code(code_index: int) -> int:
    return reduce(
        lambda previous, _: previous * 252533 % 33554393, range(code_index), 20151125
    )


def get_code_index(row: int, column: int) -> int:
    return ((row + column) * (row + column + 1)) // 2 + column
