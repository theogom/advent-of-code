from day_abstract import DayAbstract


class CPU:
    instructions: list[list[str]]
    program_counter: int
    registers: dict[str, int]

    def __init__(
        self, instructions: list[list[str]], registers: dict[str, int]
    ) -> None:
        self.instructions = instructions
        self.registers = registers
        self.program_counter = 0

    def run(self):
        while 0 <= self.program_counter < len(self.instructions):
            self.execute()

    def execute(self):
        instruction = self.instructions[self.program_counter]

        match instruction:
            case ["hlf", register]:
                self.hlf(register)

            case ["tpl", register]:
                self.tpl(register)

            case ["inc", register]:
                self.inc(register)

            case ["jmp", offset]:
                self.jmp(int(offset))

            case ["jie", register, offset]:
                self.jie(register, int(offset))

            case ["jio", register, offset]:
                self.jio(register, int(offset))

            case _:
                raise ValueError(f"Invalid instruction: {instruction}")

    def hlf(self, register: str):
        self.registers[register] //= 2
        self.program_counter += 1

    def tpl(self, register: str):
        self.registers[register] *= 3
        self.program_counter += 1

    def inc(self, register: str):
        self.registers[register] += 1
        self.program_counter += 1

    def jmp(self, offset: int):
        self.program_counter += int(offset)

    def jie(self, register: str, offset: int):
        self.program_counter += int(offset) if self.registers[register] % 2 == 0 else 1

    def jio(self, register: str, offset: int):
        self.program_counter += int(offset) if self.registers[register] == 1 else 1


class Day23(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self):
        return list(map(lambda x: x.split(" "), self.data.replace(",", "").split("\n")))

    def part_one(self, target_register="b"):
        instructions = self.parse()
        registers = {"a": 0, "b": 0}
        cpu = CPU(instructions, registers)

        cpu.run()

        return cpu.registers[target_register]

    def part_two(self, target_register="b"):
        instructions = self.parse()
        registers = {"a": 1, "b": 0}
        cpu = CPU(instructions, registers)

        cpu.run()

        return cpu.registers[target_register]
