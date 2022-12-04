from .day import DayAbstract


class Day(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self, data: str) -> list[str]:
        return list(data)

    def part_one(self) -> int:
        houses = {'0-0': 1}
        x = y = 0

        for move in self.data:
            match move:
                case '^':
                    y -= 1
                case '>':
                    x += 1
                case 'v':
                    y += 1
                case '<':
                    x -= 1
                case _:
                    raise ValueError(
                        f'Invalid move {move}, expected one of the following: ^, >, v, <'
                    )

            address = f'{x}-{y}'

            if address in houses:
                houses[address] += 1
            else:
                houses[address] = 1

        return len(houses)

    def part_two(self) -> int:
        houses = {'0-0': 2}
        santa = {'x': 0, 'y': 0}
        robot = {'x': 0, 'y': 0}

        for index, move in enumerate(self.data):
            delivery_man = santa if index % 2 == 0 else robot

            match move:
                case '^':
                    delivery_man['y'] -= 1
                case '>':
                    delivery_man['x'] += 1
                case 'v':
                    delivery_man['y'] += 1
                case '<':
                    delivery_man['x'] -= 1
                case _:
                    raise ValueError(
                        f'Invalid move {move}, expected one of the following: ^, >, v, <')

            address = f'{delivery_man["x"]}-{delivery_man["y"]}'

            if address in houses:
                houses[address] += 1
            else:
                houses[address] = 1

        return len(houses)
