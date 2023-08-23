from typing import TypedDict

from day_abstract import DayAbstract


class Grid(TypedDict):
    width: int
    height: int
    states: list[bool]


class Day18(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self) -> Grid:
        lines = self.data.split("\n")

        return {
            "width": len(lines[0]),
            "height": len(lines),
            "states": [state == "#" for state in self.data.replace("\n", "")],
        }

    def part_one(self, steps: int = 100) -> int:
        grid = self.parse()

        for _ in range(steps):
            grid["states"] = [
                get_next_state(grid, index) for index in range(len(grid["states"]))
            ]

        return grid["states"].count(True)

    def part_two(self, steps: int = 100) -> int:
        grid = self.parse()

        turn_on_corners(grid)

        for _ in range(steps):
            grid["states"] = [
                get_next_state(grid, index) for index in range(len(grid["states"]))
            ]
            turn_on_corners(grid)

        return grid["states"].count(True)


def get_next_state(grid: Grid, index: int) -> bool:
    state = grid["states"][index]
    neighbors_on_count = count_neighbors_on(grid, index)

    return state and neighbors_on_count in [2, 3] or neighbors_on_count == 3


def count_neighbors_on(grid: Grid, index: int) -> int:
    width, height, states = grid["width"], grid["height"], grid["states"]
    count = 0

    for i in range(-1, 2):
        x = index % width + i
        if x < 0 or x >= width:
            continue

        for j in range(-1, 2):
            y = index // width + j

            if y < 0 or y >= height:
                continue

            if x == index % width and y == index // width:
                continue

            count += states[y * width + x]

    return count


def grid_to_str(grid: Grid) -> str:
    string = ""

    for y in range(grid["height"]):
        for x in range(grid["width"]):
            string += "#" if grid["states"][y * grid["width"] + x] else "."
        string += "\n"

    return string


def turn_on_corners(grid: Grid) -> None:
    corners = [
        0,
        grid["width"] - 1,
        grid["width"] * (grid["height"] - 1),
        grid["width"] * grid["height"] - 1,
    ]

    for corner in corners:
        grid["states"][corner] = True
