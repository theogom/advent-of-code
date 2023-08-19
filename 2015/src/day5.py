from day_abstract import DayAbstract


VOWELS = "aeiou"
DISALLOWED = ["ab", "cd", "pq", "xy"]


class Day5(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self) -> list[str]:
        return self.data.split("\n")

    def part_one(self) -> int:
        data = self.parse()
        nice_strings = 0

        for string in data:
            # At least three different vowels
            if not sum(map(lambda vowel: string.count(vowel), VOWELS)) >= 3:
                continue

            # One letter appearing twice in a row
            for i in range(len(string) - 1):
                if string[i] == string[i + 1]:
                    break
            else:
                continue

            # Contains dissallowed strings
            if any(map(lambda substring: substring in string, DISALLOWED)):
                continue

            nice_strings += 1

        return nice_strings

    def part_two(self) -> int:
        data = self.parse()
        nice_string = 0

        for string in data:
            # Contains a pair of any two letters that appears at least twice
            for i in range(len(string) - 1):
                pair = string[i] + string[i + 1]

                if string.count(pair) >= 2:
                    break
            else:
                continue

            # Contains at least one letter which repeats with exactly one letter between them
            for i in range(len(string) - 2):
                if string[i] == string[i + 2]:
                    break
            else:
                continue

            nice_string += 1

        return nice_string
