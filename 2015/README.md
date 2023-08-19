# Advent of code 2015

Days for the [advent of code 2015](https://adventofcode.com/2015).

The project is in Python.

Solutions of each days are in the `src/days/day<index>` folder along with there test file.

The inputs are in the `inputs/` folder.

## Commands

Run all days:

```bash
make
```

Run a specific day:

```bash
make DAY=<day_number>
```

Run tests:

```bash
make tests
```

## Template

```py
from .day_abstract import DayAbstract


class Day(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self, data: str):
        return data

    def part_one(self) -> int:
        raise NotImplementedError

    def part_two(self) -> int:
        raise NotImplementedError
```
