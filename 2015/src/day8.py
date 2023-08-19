import re
from ast import literal_eval

from day_abstract import DayAbstract


class Day8(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self):
        return self.data.split("\n")

    def part_one(self) -> int:
        strings = self.parse()
        answer = 0

        for string in strings:
            answer += len(string) - len(unescape(string))

        return answer

    def part_two(self) -> int:
        strings = self.parse()
        answer = 0

        for string in strings:
            answer += len(escape(string)) - len(string)

        return answer


def unescape(string: str) -> str:
    return literal_eval(string)


def escape(string: str) -> str:
    escaped = re.sub(r'(["\\])', r"\\\1", string)
    return f'"{escaped}"'
