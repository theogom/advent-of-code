import re
from collections import defaultdict
from typing import TypedDict

from day_abstract import DayAbstract


class Input(TypedDict):
    state: str
    transitions: dict[str, list[str]]


class Day19(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self) -> Input:
        state = self.data.split("\n")[-1]
        transitions = defaultdict(list)

        for current_state, next_state in re.findall(r"(\w+) => (\w+)", self.data):
            transitions[current_state].append(next_state)

        return {
            "state": state,
            "transitions": transitions,
        }

    def part_one(self):
        data = self.parse()

        initial_state, transitions = data["state"], data["transitions"]
        next_states = get_next_states(initial_state, transitions)

        return len(set(next_states))

    def part_two(self):
        state = self.data.split("\n")[-1][::-1]
        reversed_transitions = {
            next_state[::-1]: current_state[::-1]
            for current_state, next_state in re.findall(r"(\w+) => (\w+)", self.data)
        }

        step = 0
        replacements = "|".join(reversed_transitions.keys())

        while state != "e":
            state = re.sub(
                replacements, lambda x: reversed_transitions[x.group()], state, 1
            )
            step += 1

        return step


def get_next_states(current_state: str, transitions: dict[str, list[str]]):
    for key, replacements in transitions.items():
        key_index = current_state.find(key)
        while key_index != -1:
            for replacement in replacements:
                yield splice(current_state, key_index, len(key), replacement)

            key_index = current_state.find(key, key_index + 1)


def splice(string: str, start: int, deleteCount: int, inserted: str) -> str:
    return f"{string[:start]}{inserted}{string[start + deleteCount:]}"
