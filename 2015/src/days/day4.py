from .day import DayAbstract

from hashlib import md5


class Day(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self, data: str) -> str:
        return data

    def part_one(self) -> int:
        key = self.data
        i = 0

        while True:
            string = f'{key}{i}'
            md5hash = md5(string.encode()).hexdigest()

            if md5hash[:5] == '0' * 5:
                return i

            i += 1

    def part_two(self) -> int:
        key = self.data
        i = 0

        while True:
            string = f'{key}{i}'
            md5hash = md5(string.encode()).hexdigest()

            if md5hash[:6] == '0' * 6:
                return i

            i += 1
