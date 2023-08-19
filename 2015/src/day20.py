from collections import defaultdict
from math import sqrt

from day_abstract import DayAbstract


class Day20(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self) -> int:
        return int(self.data)

    def part_one(self):
        target_present_count = self.parse()
        house_number = 0
        present_count = 0

        while present_count < target_present_count:
            house_number += 1
            present_count = 0

            for divisor in get_divisors(house_number):
                present_count += divisor * 10

        return house_number

    def part_two(self):
        target_present_count = self.parse()
        house_number = 0
        present_count = 0
        elfs = defaultdict(lambda: 0)

        while present_count < target_present_count:
            house_number += 1
            present_count = 0

            for divisor in get_divisors(house_number):
                if elfs[divisor] == 50:
                    continue

                present_count += divisor * 11
                elfs[divisor] += 1

        return house_number


def get_divisors(number: int):
    for i in range(1, int(sqrt(number) + 1)):
        if number % i == 0:
            yield i
            if i * i != number:
                yield number // i
