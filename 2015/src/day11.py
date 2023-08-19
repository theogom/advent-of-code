import re

from day_abstract import DayAbstract


class Day11(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self, data: str):
        return data

    def part_one(self) -> str:
        password = get_next_password(self.data)
        while not is_password_valid(password):
            password = get_next_password(password)

        return password

    def part_two(self) -> str:
        password = get_next_password(self.part_one())

        while not is_password_valid(password):
            password = get_next_password(password)

        return password


def get_next_password(previous_password):
    return encode(decode(previous_password) + 1)


def is_password_valid(password):
    return (
        has_consecutive_letters(password, 3)
        and has_not_invalid_letter(password, ["i", "l", "o"])
        and has_different_pairs(password, 2)
    )


def has_consecutive_letters(password: str, consecutive_letters: int) -> bool:
    ords = list(map(ord, password))
    count = 1

    for i in range(len(ords) - 1):
        if ords[i] + 1 == ords[i + 1]:
            count += 1
            if count == consecutive_letters:
                return True
        else:
            count = 1

    return False


def has_not_invalid_letter(password: str, invalid_chars: list[str]) -> bool:
    return not re.search(rf'[{"".join(invalid_chars)}]', password)


def has_different_pairs(password: str, pairs_count: int) -> bool:
    return len(set(re.findall(r"([a-z])\1", password))) >= pairs_count


def decode(encoded: str) -> int:
    """
    Decode a lowercase letter string to a number using a base-26 system with 1-based indexing.
    Given the following series: a, b, c, ..., z, aa, ab, ac, ..., az, ba, bb, ...,
    the output is the index of the string in the series (1-based indexed),
    e.g.: a = 1, b = 2, ..., z = 26, aa = 27, ab = 28, ....
    """
    base = ord("a") - 1  # ASCII value of 'a' minus 1
    decoded = 0

    for i, char in enumerate(encoded[::-1]):
        decoded += (ord(char) - base) * 26**i

    return decoded


def encode(decoded: int) -> str:
    """
    Encode a number to a lowercase letter string using a base-26 system with 1-based indexing.
    Given the number, the output is the index of the string in the series (1-based indexed):
    a, b, c, ..., z, aa, ab, ac, ..., az, ba, bb, ...,
    """
    base = ord("a")  # ASCII value of 'a'

    encoded = ""
    while decoded > 0:
        remainder = (decoded - 1) % 26
        char = chr(base + remainder)
        encoded = char + encoded
        decoded = (decoded - 1) // 26

    return encoded
