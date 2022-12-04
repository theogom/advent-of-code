from sys import argv
import days

USAGE = 'Usage: make [DAY=<day_number>]'
INPUTS_DIR = 'inputs'


def day_header(index: int) -> str:
    return f'--- Day {index} ---'


def run(index: int) -> None:
    if not isinstance(index, int):
        raise ValueError(f'index must be an int, ${type(index)} found.')

    print(day_header(index))

    try:
        module = getattr(days, f'day{index}')
    except AttributeError:
        print(f'Day {index} not found, available days: {" , ".join(map(lambda day: day.split("day")[1], days.__all__))}')
        return
    try:
        with open(f'{INPUTS_DIR}/input{index}.txt') as file:
            data = file.read()
    except FileNotFoundError:
        print(f'No input file found for day {index}.')
        return
    except Exception as e:
        print(f'Error while reading input file for day {index}: {e}')
        return

    day = module.Day(data)

    print(day.part_one())
    print(day.part_two())


def run_all() -> None:
    for index in range(1, len(days.__all__) + 1):
        try:
            run(index)
        except Exception as e:
            print(f'Error while running day {index}: {e}')


if __name__ == '__main__':
    if len(argv) < 2 or argv[1] != '--day':
        run_all()
        exit()

    if len(argv) < 3:
        print('Day number missing.')
        print(USAGE)
        exit(1)

    if not argv[2].isnumeric():
        print(f'Invalid day number: {argv[2]}')
        print(USAGE)
        exit(1)
    
    index = int(argv[2])

    if index < 1 or index > 25:
        print(f'Invalid day number {index}, day number must be between 1 and 25.')
        print(USAGE)
        exit(1)

    run(index)
