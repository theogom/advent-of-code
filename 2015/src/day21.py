import re
from itertools import chain, combinations, product
from functools import reduce
from typing import Callable, TypedDict

from day_abstract import DayAbstract


class Item(TypedDict):
    armor: int
    cost: int
    damage: int


class Shop(TypedDict):
    armors: list[Item]
    rings: list[Item]
    weapons: list[Item]


class Player:
    armor: int
    damage: int
    hit_points: int

    def __init__(self, armor=0, damage=0, hit_points=100) -> None:
        self.armor = armor
        self.damage = damage
        self.hit_points = hit_points

    def equip(self, items: list[Item]) -> None:
        self.armor = reduce(lambda armor, item: armor + item["armor"], items, 0)
        self.damage = reduce(lambda damage, item: damage + item["damage"], items, 0)

    def is_dead(self):
        return self.hit_points <= 0

    def defend(self, damage: int):
        self.hit_points -= max(damage - self.armor, 1)


def create_item(armor: int, cost: int, damage: int) -> Item:
    return {
        "armor": armor,
        "cost": cost,
        "damage": damage,
    }


shop: Shop = {
    "armors": [
        create_item(1, 13, 0),
        create_item(2, 31, 0),
        create_item(3, 53, 0),
        create_item(4, 75, 0),
        create_item(5, 102, 0),
    ],
    "rings": [
        create_item(0, 25, 1),
        create_item(0, 50, 2),
        create_item(0, 100, 3),
        create_item(1, 20, 0),
        create_item(2, 40, 0),
        create_item(3, 80, 0),
    ],
    "weapons": [
        create_item(0, 8, 4),
        create_item(0, 10, 5),
        create_item(0, 25, 6),
        create_item(0, 40, 7),
        create_item(0, 74, 8),
    ],
}


class Day21(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self) -> Player:
        hit_points, damage, armor = map(int, re.findall(r"\d+", self.data))

        return Player(armor=armor, damage=damage, hit_points=hit_points)

    def part_one(self):
        def win(items: list[Item]):
            boss = self.parse()
            player = Player()
            player.equip(list(items))

            return fight(player, boss)

        combinations = get_item_combinations()
        winning_combinations = list(filter(win, combinations))
        costs = map(get_items_cost, winning_combinations)
        return min(costs)

    def part_two(self):
        def win(items: list[Item]):
            boss = self.parse()
            player = Player()
            player.equip(list(items))

            return fight(player, boss)

        combinations = get_item_combinations()
        winning_combinations = list(filter(lambda c: not win(c), combinations))
        costs = map(get_items_cost, winning_combinations)
        return max(costs)


def get_item_combinations():
    armors = [c for i in range(2) for c in combinations(shop["armors"], i)]
    rings = [c for i in range(3) for c in combinations(shop["rings"], i)]
    weapons = list(combinations(shop["weapons"], 1))
    return tuple(
        map(lambda x: list(chain.from_iterable(x)), product(armors, rings, weapons))
    )


def get_items_cost(items):
    return reduce(lambda cost, item: cost + item["cost"], items, 0)


def fight(p1: Player, p2: Player) -> bool:
    while True:
        p2.defend(p1.damage)

        if p2.is_dead():
            return True

        p1.defend(p2.damage)

        if p1.is_dead():
            return False
