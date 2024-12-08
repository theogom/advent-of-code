import { DayAbstract } from '../utils/day';

type Input = number[][][];

export class Day extends DayAbstract {
    parse(input: string): Input {
        return input
            .split('\n')
            .map((line) =>
                line.split(',').map((section) => section.split('-').map(Number))
            );
    }

    partOne(): number {
        return this.input.reduce(
            (acc: number, sections: number[][]) =>
                acc +
                Number(
                    (sections[0][0] <= sections[1][0] &&
                        sections[0][1] >= sections[1][1]) ||
                        (sections[0][0] >= sections[1][0] &&
                            sections[0][1] <= sections[1][1])
                ),
            0
        );
    }

    partTwo(): number {
        return this.input.reduce(
            (acc: number, sections: number[][]) =>
                acc +
                Number(
                    (sections[0][0] >= sections[1][0] &&
                        sections[0][0] <= sections[1][1]) ||
                        (sections[0][1] >= sections[1][0] &&
                            sections[0][1] <= sections[1][1]) ||
                        (sections[1][0] >= sections[0][0] &&
                            sections[1][0] <= sections[0][1]) ||
                        (sections[1][1] >= sections[0][0] &&
                            sections[1][1] <= sections[0][1])
                ),
            0
        );
    }
}
