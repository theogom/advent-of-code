import { DayAbstract } from '../utils/day';

type Input = number[][];

export class Day extends DayAbstract {
    parse(input: string): Input {
        return input.split('\n\n').map((line) => line.split('\n').map(Number));
    }

    partOne() {
        return this.input
            .map((numbers: number[]) =>
                numbers.reduce((acc: number, num: number) => acc + num, 0)
            )
            .reduce((max: number, num: number) => (max > num ? max : num), 0);
    }

    partTwo() {
        return this.input
            .map((numbers: number[]) =>
                numbers.reduce((acc: number, num: number) => acc + num, 0)
            )
            .sort((a: number, b: number) => b - a)
            .slice(0, 3)
            .reduce((acc: number, num: number) => acc + num, 0);
    }
}
