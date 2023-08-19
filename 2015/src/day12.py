import json
import re

from typing import Callable

from day_abstract import DayAbstract

Json = dict | list


class Day12(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self, data: str) -> str:
        return data

    def part_one(self) -> int:
        return sum(map(int, re.findall(r"-?\d+", self.data)))

    def part_two(self) -> int:
        data = json.loads(self.data)

        return sum_from_json(
            data, lambda x: isinstance(x, dict) and "red" in x.values()
        )


def sum_from_json(data: Json, exclude: Callable[[Json], bool] | None = None) -> int:
    values = data.values() if isinstance(data, dict) else data

    if exclude and exclude(data):
        return 0

    count = 0

    for value in values:
        match value:
            case int():
                count += value
            case dict():
                count += sum_from_json(value, exclude)
            case list():
                count += sum_from_json(value, exclude)

    return count
