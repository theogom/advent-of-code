import re

from day_abstract import DayAbstract

TIME_LIMIT = 2503


class Reindeer:
    distance: int
    iteration: int
    fly_time: int
    rest_time: int
    speed: int

    def __init__(self, fly_time: int, rest_time: int, speed: int) -> None:
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.speed = speed

        self.distance = 0
        self.iteration = 0

    def get_total_distance(self, time_limit: int) -> int:
        total_fly_time = self.fly_time * (
            time_limit // (self.fly_time + self.rest_time)
        )
        total_fly_time += min(
            time_limit % (self.fly_time + self.rest_time), self.fly_time
        )

        return self.speed * total_fly_time

    def advance(self) -> None:
        if not self.is_resting():
            self.distance += self.speed

        self.iteration += 1

    def is_resting(self) -> bool:
        return self.iteration % (self.fly_time + self.rest_time) >= self.fly_time


class Day14(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self) -> list[Reindeer]:
        reindeers: list[Reindeer] = []

        for line in self.data.split("\n"):
            speed, fly_time, rest_time = map(int, re.findall(r"\d+", line))

            reindeers.append(
                Reindeer(
                    fly_time,
                    rest_time,
                    speed,
                )
            )

        return reindeers

    def part_one(self) -> int:
        return max(map(lambda x: x.get_total_distance(TIME_LIMIT), self.parse()))

    def part_two(self) -> int:
        reindeers = self.parse()
        points = [0] * len(reindeers)

        for i in range(TIME_LIMIT):
            for reindeer in reindeers:
                reindeer.advance()

            leaders = get_leaders(reindeers)

            for leader in leaders:
                points[leader] += 1

        return max(points)


def get_leaders(reindeers: list[Reindeer]):
    if len(reindeers) == 0:
        return []

    distances = list(map(lambda x: x.distance, reindeers))
    max_distance = distances[0]
    leaders = [0]

    for i, distance in enumerate(distances[1:]):
        if distance == max_distance:
            leaders.append(i + 1)

        if distance > max_distance:
            leaders = [i + 1]
            max_distance = distance

    return leaders
