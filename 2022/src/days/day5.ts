import { DayAbstract } from '../utils/day';

type Crate = string;

type Rearrangement = {
    amount: number;
    from: number;
    to: number;
};

type Input = { stacks: Crate[][]; rearrangements: Rearrangement[] };

export class Day extends DayAbstract {
    input!: Input;

    parse(input: string): Input {
        const splits = input.split('\n\n');
        const levels = splits[0].split('\n').slice(0, -1);

        const stacksNumber =
            levels[levels.length - 1].match(/.{1,4}/g)?.length ?? 0;

        const stacks: Crate[][] = Array.from(Array(stacksNumber), () => []);

        for (let level of levels) {
            for (let [index, str] of (level.match(/.{1,4}/g) ?? []).entries()) {
                const crate = str.trim();

                if (crate) {
                    stacks[index].push(crate[1]);
                }
            }
        }

        const rearrangements = splits[1].split('\n').map((rearrangement) => {
            const [amount, from, to] = rearrangement
                .split(/move | from | to /)
                .slice(1)
                .map(Number);

            return {
                amount,
                from,
                to,
            };
        });

        return {
            stacks,
            rearrangements,
        };
    }

    partOne(): string {
        const { rearrangements } = this.input;
        const stacks = this.input.stacks.map((stack) => [...stack]);

        for (let { amount, from, to } of rearrangements) {
            const crates = stacks[from - 1].splice(0, amount);
            stacks[to - 1].unshift(...crates.reverse());
        }

        return stacks.map((stack) => stack[0]).join('');
    }

    partTwo(): string {
        const { rearrangements } = this.input;
        const stacks = this.input.stacks.map((stack) => [...stack]);

        for (let { amount, from, to } of rearrangements) {
            const crates = stacks[from - 1].splice(0, amount);
            stacks[to - 1].unshift(...crates);
        }

        return stacks.map((stack) => stack[0]).join('');
    }
}
