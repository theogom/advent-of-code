import re
from itertools import product

from day_abstract import DayAbstract


class Day15(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self) -> list[dict]:
        def extract(line: str) -> dict:
            ingredient = re.split(": |, ", line)

            return {
                "name": ingredient[0],
                "capacity": int(ingredient[1].split(" ")[1]),
                "durability": int(ingredient[2].split(" ")[1]),
                "flavor": int(ingredient[4].split(" ")[1]),
                "texture": int(ingredient[3].split(" ")[1]),
                "calories": int(ingredient[5].split(" ")[1]),
            }

        return list(map(extract, self.data.split("\n")))

    def part_one(self) -> int:
        ingredients = self.parse()

        combinations = product(range(101), repeat=len(ingredients))
        combinations = filter(lambda combination: sum(combination) == 100, combinations)

        return max(get_scores(ingredients, combinations))

    def part_two(self) -> int:
        ingredients = self.parse()

        combinations = product(range(101), repeat=len(ingredients))
        combinations = filter(lambda combination: sum(combination) == 100, combinations)

        return max(get_scores(ingredients, combinations, 500))


def get_scores(ingredients, combinations, target_calories=None):
    for combination in combinations:
        yield get_score(ingredients, combination, target_calories)


def get_score(ingredients, quantities, target_calories=None):
    score = 1
    properties = ["capacity", "durability", "flavor", "texture"]

    if target_calories is not None:
        calories = 0
        for i, ingredient in enumerate(ingredients):
            calories += ingredient["calories"] * quantities[i]

        if calories != target_calories:
            return 0

    for prop in properties:
        prop_score = 0
        for i, ingredient in enumerate(ingredients):
            prop_score += ingredient[prop] * quantities[i]

        score *= max(0, prop_score)

    return score
