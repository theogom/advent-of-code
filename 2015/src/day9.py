from day_abstract import DayAbstract
from typing import TypedDict
from itertools import permutations


City = str


class Input(TypedDict):
    cities: set[City]
    distances: dict[str, int]


class Day9(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self) -> Input:
        cities = set()
        distances = {}

        for line in self.data.split("\n"):
            # London to Dublin = 464
            src, _, dst, _, length = line.split(" ")
            tripId = src + dst if src < dst else dst + src
            distances[tripId] = int(length)
            cities.add(src)
            cities.add(dst)

        return {
            "cities": cities,
            "distances": distances,
        }

    def part_one(self) -> int:
        data = self.parse()
        distances = []

        for cities in permutations(data["cities"]):
            distance = 0

            for i in range(0, len(cities) - 1):
                tripId = (
                    cities[i] + cities[i + 1]
                    if cities[i] < cities[i + 1]
                    else cities[i + 1] + cities[i]
                )
                distance += data["distances"][tripId]

            distances.append(distance)

        return min(distances)

    def part_two(self) -> int:
        data = self.parse()
        distances = []

        for cities in permutations(data["cities"]):
            distance = 0

            for i in range(0, len(cities) - 1):
                tripId = (
                    cities[i] + cities[i + 1]
                    if cities[i] < cities[i + 1]
                    else cities[i + 1] + cities[i]
                )
                distance += data["distances"][tripId]

            distances.append(distance)

        return max(distances)
