from itertools import chain, combinations

from day_abstract import DayAbstract


class Day17(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self):
        return list(map(int, self.data.split("\n")))

    def part_one(self, capacity: int = 150) -> int:
        containers = self.parse()

        containers_combinations = chain(
            combination
            for length in range(len(containers))
            for combination in combinations(containers, length)
        )

        fitting_containers_combinations = list(
            filter(lambda c: sum(c) == capacity, containers_combinations)
        )

        return len(fitting_containers_combinations)

    def part_two(self, capacity: int = 150) -> int:
        containers = self.parse()

        containers_combinations = chain(
            combination
            for length in range(len(containers))
            for combination in combinations(containers, length)
        )

        fitting_containers_combinations = list(
            filter(lambda c: sum(c) == capacity, containers_combinations)
        )

        min_container_count = min(map(len, fitting_containers_combinations))

        minimal_containers_combinations = list(
            filter(
                lambda c: len(c) == min_container_count, fitting_containers_combinations
            )
        )

        return len(minimal_containers_combinations)
