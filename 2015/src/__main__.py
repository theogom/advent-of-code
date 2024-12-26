import logging
from sys import argv
from importlib import import_module

USAGE = "usage: python3 main.py [--day <day_number>]"
INPUTS_DIR = "inputs"
NOT_IMPLEMENTED = "=> not implemented"

logging.basicConfig(format="%(name)s:%(levelname)s:%(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_day(index: int):
    module = import_module(f"day{index}")
    return getattr(module, f"Day{index}")


def get_input(index: int):
    with open(f"{INPUTS_DIR}/input{index}.txt") as file:
        return file.read()


def run(index: int) -> None:
    try:
        Day = get_day(index)
    except AttributeError:
        logger.error(f"Class Day{index} not found")
        return
    # except ModuleNotFoundError:
    #     logger.error(f"day {index} not found or contains import errors")
    #     return

    try:
        data = get_input(index)
    except FileNotFoundError:
        logger.error(f"no input file found for day {index}.")
        return
    except Exception as e:
        logger.error(f"error while reading input file for day {index}: {e}")
        return

    day = Day(data)

    print(f"Day {index}")

    try:
        print(f"=> {day.part_one()}")
    except NotImplementedError:
        print(NOT_IMPLEMENTED)

    try:
        print(f"=> {day.part_two()}")
    except NotImplementedError:
        print(NOT_IMPLEMENTED)


def run_all() -> None:
    for index in range(1, 26):
        try:
            run(index)
            print()
        except Exception as e:
            logger.error(f"day {index}: {e}")


if __name__ == "__main__":
    if len(argv) < 2 or argv[1] != "--day":
        run_all()
        exit()

    if len(argv) < 3:
        logger.error("Day number missing")
        print(USAGE)
        exit(1)

    if not argv[2].isnumeric():
        logger.error(f"Invalid day number: {argv[2]}")
        print(USAGE)
        exit(1)

    index = int(argv[2])

    if index < 1 or index > 25:
        logger.error(f"Invalid day number {index}, day number must be between 1 and 25")
        print(USAGE)
        exit(1)

    run(index)
