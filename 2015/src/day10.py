from day_abstract import DayAbstract


class Day10(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self, data: str):
        return data

    def part_one(self) -> int:
        look_string = self.data

        for _ in range(40):
            look_string = look_and_say(look_string)

        return len(look_string)

    def part_two(self) -> int:
        look_string = self.data

        for _ in range(50):
            look_string = look_and_say(look_string)

        return len(look_string)


def look_and_say(look_string: str) -> str:
    say_string = ""

    i = 0
    while i < len(look_string):
        current_char = look_string[i]
        char = current_char
        count = 0

        while char == current_char:
            count += 1
            i += 1

            if i >= len(look_string):
                break

            char = look_string[i]

        say_string += f"{count}{current_char}"

    return say_string
