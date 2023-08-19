from typing import Callable, TypedDict

from day_abstract import DayAbstract

MASK = 0xFFFF

Signal = int
Wire = str


class Expression(TypedDict):
    operator: Callable
    l_operand: int | str | None
    r_operand: int | str | None


class Day7(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self) -> dict[Wire, Expression]:
        instructions = self.data.split("\n")
        expressions = {}

        for instruction in instructions:
            expression, wire = instruction.split(" -> ")
            expressions[wire] = parse_expression(expression.split(" "))

        return expressions

    def part_one(self, target="a") -> Signal:
        expressions = self.parse()

        return evaluate(expressions, target, {})

    def part_two(self, target_1="a", target_2="b") -> Signal:
        expressions = self.parse()

        signal = evaluate(expressions, target_1, {})

        expressions[target_2] = {
            "operator": operators["NONE"],
            "l_operand": signal,
            "r_operand": None,
        }

        return evaluate(expressions, target_1, {})


operators = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "NOT": lambda _, y: ~y & MASK,
    "LSHIFT": lambda x, y: (x << y) & MASK,
    "RSHIFT": lambda x, y: (x >> y) & MASK,
    "NONE": lambda x, _: x,
}


def evaluate(
    expressions: dict[Wire, Expression], target: Wire, cache: dict[Wire, Signal]
):
    assert target in expressions, f"Unknown wire {target}"

    if target in cache:
        return cache[target]

    expression = expressions[target]
    l_operand, r_operand = (
        evaluate(expressions, operand, cache) if isinstance(operand, Wire) else operand
        for operand in (expression["l_operand"], expression["r_operand"])
    )

    signal = expression["operator"](l_operand, r_operand)
    cache[target] = signal

    return signal


def parse_expression(expression: list[str]) -> Expression:
    match len(expression):
        case 1:
            [operand] = expression

            return {
                "operator": operators["NONE"],
                "l_operand": parse_operand(operand),
                "r_operand": None,
            }
        case 2:
            gate, operand = expression

            assert (
                gate == "NOT"
            ), f"Invalid gate {gate} for length-2 expression {expression}"

            return {
                "operator": operators[gate],
                "l_operand": None,
                "r_operand": parse_operand(operand),
            }
        case 3:
            l_operand, gate, r_operand = expression
            operator = operators.get(gate)

            if operator is None:
                raise ValueError(f"Invalid gate {gate} in {expression}")

            return {
                "operator": operator,
                "l_operand": parse_operand(l_operand),
                "r_operand": parse_operand(r_operand),
            }
        case _:
            raise ValueError(f"Invalid expression {expression}")


def parse_operand(operand: str) -> Wire | Signal:
    return Signal(operand) if operand.isdigit() else operand
