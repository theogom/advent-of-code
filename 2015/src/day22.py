import re
from dataclasses import dataclass

from day_abstract import DayAbstract


@dataclass
class Spell:
    name: str
    cost: int
    armor: int = 0
    damage: int = 0
    duration: int = 0
    heal: int = 0
    mana: int = 0


Effect = tuple[Spell, int]


@dataclass
class Player:
    damage: int
    hit_points: int


@dataclass
class Wizard(Player):
    armor: int
    mana: int


@dataclass
class State:
    boss: Player
    player: Wizard
    effects: list[Effect]
    states: list["State"]
    transitions: list[Spell]
    cost: int

    @staticmethod
    def copy(state: "State") -> "State":
        return State(
            boss=Player(damage=state.boss.damage, hit_points=state.boss.hit_points),
            player=Wizard(
                armor=state.player.armor,
                mana=state.player.mana,
                damage=state.player.damage,
                hit_points=state.player.hit_points,
            ),
            effects=[*state.effects],
            states=[*state.states],
            transitions=[*state.transitions],
            cost=state.cost,
        )


class Day22(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self) -> Player:
        hit_points, damage = map(int, re.findall(r"\d+", self.data))

        return Player(damage=damage, hit_points=hit_points)

    def part_one(self) -> int:
        boss = self.parse()
        player = Wizard(armor=0, mana=500, damage=0, hit_points=50)
        initial_state = State(
            boss=boss, player=player, effects=[], states=[], transitions=[], cost=0
        )
        state = search(initial_state)

        if not state:
            return -1

        # print_state(state)

        return state.cost

    def part_two(self) -> int:
        boss = self.parse()
        player = Wizard(armor=0, mana=500, damage=0, hit_points=50)
        initial_state = State(
            boss=boss, player=player, effects=[], states=[], transitions=[], cost=0
        )
        state = search(initial_state, hard=True)

        if not state:
            return -1

        # print_state(state)

        return state.cost


spells = [
    Spell(name="Magic Missile", cost=53, damage=4),
    Spell(name="Drain", cost=73, damage=2, heal=2),
    Spell(name="Shield", cost=113, duration=6, armor=7),
    Spell(name="Poison", cost=173, duration=6, damage=3),
    Spell(name="Recharge", cost=229, duration=5, mana=101),
]


def search(initial_state: State, hard: bool = False) -> State | None:
    """
    Use depth-first search with pruning to find the optimal game,
    i.e. the game with the minimal cost.
    """
    stack: list[tuple[State, bool]] = [(initial_state, False)]
    optimal_state = None

    while stack:
        current_state, is_processed = stack.pop()

        if is_processed:
            if not is_final(current_state):
                continue

            if not has_won(current_state):
                continue

            if optimal_state and current_state.cost >= optimal_state.cost:
                continue

            optimal_state = current_state

            continue

        stack.append((current_state, True))

        if is_final(current_state):
            continue

        transitions = get_transitions(
            current_state, optimal_state.cost if optimal_state else None
        )

        for transition in transitions:
            next_state = apply_transition(State.copy(current_state), transition, hard)
            next_state.states.append(next_state)
            next_state.transitions.append(transition)

            stack.append((next_state, False))

    return optimal_state


def apply_transition(state: State, transition: Spell, hard: bool) -> State:
    """
    Apply a transition to the state.
    """
    if hard:
        state.player.hit_points -= 1

        if is_final(state):
            return state

    state = apply_effects(state)

    if is_final(state):
        return state

    state = apply_spell(state, transition)

    if is_final(state):
        return state

    state = apply_effects(state)

    if is_final(state):
        return state

    state = apply_boss(state)
    return state


def apply_effects(state: State) -> State:
    """
    Apply effects to the state.
    Reduce the duration of each effect by 1.
    """
    remaining_effects: list[Effect] = []

    armor = 0
    damage = 0
    heal = 0
    mana = 0

    for effect, duration in state.effects:
        armor = max(armor, effect.armor)
        damage += effect.damage
        heal += effect.heal
        mana += effect.mana

        if duration > 1:
            remaining_effects.append((effect, duration - 1))

    state.boss.hit_points -= damage

    state.player.armor = armor
    state.player.hit_points += heal
    state.player.mana += mana

    state.effects = remaining_effects

    return state


def apply_spell(state: State, spell: Spell) -> State:
    """
    Apply spell to a state.
    If the spell is an effect, add it to the list of effects.
    Otherwise, apply the spell instantly.
    """
    if spell.duration > 0:
        state.effects.append((spell, spell.duration))
    else:
        state.boss.hit_points -= spell.damage
        state.player.hit_points += spell.heal

    state.player.mana -= spell.cost
    state.cost += spell.cost

    return state


def apply_boss(state: State) -> State:
    """
    Apply boss attack to a state.
    """
    state.player.hit_points -= max(1, state.boss.damage - state.player.armor)

    return state


def get_transitions(state: State, minimal_cost: int | None) -> list[Spell]:
    """
    Get all possible transitions (i.e. spells) from the given state.
    Discard the transitions:
    - which would exceeds current minimal cost
    - which are unaffordable
    - which would apply an effect that is already active
    """
    transitions: list[Spell] = []

    for spell in spells:
        # Discard transition which would exceeds current minimal cost
        if minimal_cost is not None and state.cost + spell.cost >= minimal_cost:
            continue

        # Discard unaffordable transition
        if spell.cost >= state.player.mana:
            continue

        # Discard transition which would apply an effect that is already active
        if any(map(lambda x: x[1] > 1 and x[0].name == spell.name, state.effects)):
            continue

        transitions.append(spell)

    return transitions


def is_final(state: State) -> bool:
    """
    Check if the game is over (either the player or the boss is dead).
    """
    return any(map(lambda x: x.hit_points <= 0, [state.boss, state.player]))


def has_won(state: State) -> bool:
    """
    Check if the player has won the game.
    """
    if state.boss.hit_points <= 0 and state.player.hit_points <= 0:
        raise Exception("Both the player and the boss are dead.")

    return state.player.hit_points > 0


def print_state(state: State) -> None:
    print(
        *map(
            lambda t: t.name,
            state.transitions,
        ),
        sep=" -> ",
    )
