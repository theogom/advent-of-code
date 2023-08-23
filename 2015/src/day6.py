from day_abstract import DayAbstract


class Day6(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self) -> list[dict]:
        instructions = []

        for line in self.data.split("\n"):
            strings = line.split(" ")

            if (len(strings)) == 5:
                command, switch, start, _, end = strings
            else:
                command, start, _, end = strings
                switch = None

            instruction = {}
            instruction["command"] = command
            instruction["switch"] = switch
            coords = start.split(",")
            instruction["start"] = {"x": int(coords[0]), "y": int(coords[1])}
            coords = end.split(",")
            instruction["end"] = {"x": int(coords[0]), "y": int(coords[1])}
            instructions.append(instruction)

        return instructions

    def part_one(self) -> int:
        instuctions = self.parse()
        dimension = 1000
        grid = [False for _ in range(dimension * dimension)]

        for instuction in instuctions:
            for y in range(instuction["start"]["y"], instuction["end"]["y"] + 1):
                for x in range(instuction["start"]["x"], instuction["end"]["x"] + 1):
                    index = y * dimension + x
                    grid[index] = (
                        not grid[index]
                        if instuction["command"] == "toggle"
                        else instuction["switch"] == "on"
                    )

        return grid.count(True)

    def part_two(self) -> int:
        instuctions = self.parse()
        dimension = 1000
        grid = [0 for _ in range(dimension * dimension)]

        for instuction in instuctions:
            for y in range(instuction["start"]["y"], instuction["end"]["y"] + 1):
                for x in range(instuction["start"]["x"], instuction["end"]["x"] + 1):
                    index = y * dimension + x
                    grid[index] += (
                        2
                        if instuction["command"] == "toggle"
                        else 1
                        if instuction["switch"] == "on"
                        else -1
                    )

                    if grid[index] < 0:
                        grid[index] = 0

        return sum(grid)
