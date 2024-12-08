import { DayAbstract } from '../utils/day';

type Input = string;

export class Day extends DayAbstract {
    parse(input: string): Input {
        return input;
    }

    partOne(): number {
        return findMarker(this.input, 4);
    }

    partTwo(): number {
        return findMarker(this.input, 14);
    }
}

function findMarker(str: string, length: number): number {
    let cursor = 0;

    for (let i = 1; i < str.length; i++) {
        const char = str[i];
        const marker = str.slice(cursor, i);
        const duplicateIndex = marker.indexOf(char);

        if (duplicateIndex !== -1) {
            cursor += duplicateIndex + 1;
        } else if (i + 1 - cursor === length) {
            return i + 1;
        }
    }

    return -1;
}
