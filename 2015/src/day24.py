from functools import reduce
from itertools import combinations
from operator import mul

from day_abstract import DayAbstract


class Day24(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self):
        return list(map(int, self.data.split("\n")))

    def part_one(self):
        weights = self.parse()
        group_weight = sum(weights) // 3
        return get_minimal_quantum_entanglements(weights, group_weight)

    def part_two(self):
        weights = self.parse()
        group_weight = sum(weights) // 4
        return get_minimal_quantum_entanglements(weights, group_weight)


def get_minimal_quantum_entanglements(weights: list[int], group_weight: int):
    groups = get_minimal_length_groups(weights, group_weight)
    return get_quantum_entanglement(groups[0])


def get_minimal_length_groups(weights: list[int], group_weight: int):
    for i in range(1, len(weights)):
        groups = tuple(
            filter(lambda x: sum(x) == group_weight, combinations(weights, i))
        )

        if len(groups) > 0:
            return groups

    return tuple()


def get_quantum_entanglement(group: tuple[int]):
    return reduce(mul, group)
