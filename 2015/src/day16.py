import re
from typing import Callable

from day_abstract import DayAbstract

Aunt = dict[str, int]

TARGET_AUNT: Aunt = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


class Day16(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self) -> list[Aunt]:
        def parse_aunt(line: str) -> Aunt:
            matches = re.findall(r"([a-z]*): (\d+)", line)
            matches = map(lambda match: (match[0], int(match[1])), matches)
            return dict(matches)

        return list(map(parse_aunt, self.data.split("\n")))

    def part_one(self) -> int:
        aunts = self.parse()

        def get_intersection(aunt_1: Aunt, aunt_2: Aunt) -> Aunt:
            return {
                key: aunt_1[key]
                for key in aunt_1
                if key in aunt_2 and aunt_1[key] == aunt_2[key]
            }

        return find_aunt(aunts, get_intersection)

    def part_two(self) -> int:
        aunts = self.parse()

        def get_intersection(aunt_1: Aunt, aunt_2: Aunt) -> Aunt:
            def matched(key, value_1, value_2):
                match key:
                    case "cats" | "trees":
                        return value_1 > value_2
                    case "goldfish" | "pomeranians":
                        return value_1 < value_2
                    case _:
                        return value_1 == value_2

            return {
                key: aunt_1[key]
                for key in aunt_1
                if key in aunt_2 and matched(key, aunt_1[key], aunt_2[key])
            }

        return find_aunt(aunts, get_intersection)


def find_aunt(aunts: list[Aunt], get_intersection: Callable[[Aunt, Aunt], Aunt]):
    aunt_number = 0
    max_intersection_length = 0
    for aunt_index, aunt in enumerate(aunts):
        intersection_length = len(get_intersection(aunt, TARGET_AUNT))

        if intersection_length > max_intersection_length:
            max_intersection_length = intersection_length
            aunt_number = aunt_index + 1

    return aunt_number
