import { DayAbstract } from '../utils/day';

type Input = string[];

function itemToPriority(item: string): number {
    const charCode = item.charCodeAt(0);

    return item === item.toLowerCase()
        ? charCode - 'a'.charCodeAt(0) + 1
        : charCode - 'A'.charCodeAt(0) + 27;
}

export class Day extends DayAbstract {
    parse(input: string): Input {
        return input.split('\n');
    }

    partOne() {
        let sum = 0;

        for (let rucksack of this.input) {
            const compartments = [
                rucksack.slice(0, rucksack.length / 2),
                rucksack.slice(rucksack.length / 2),
            ];
            let itemToFind;

            for (let item of compartments[0]) {
                if (compartments[1].includes(item)) {
                    itemToFind = item;
                }
            }

            sum += itemToPriority(itemToFind);
        }

        return sum;
    }

    partTwo() {
        let sum = 0;

        for (let i = 0; i < this.input.length; i += 3) {
            const rucksacks = this.input.slice(i, i + 3);
            let itemToFind;

            for (let item of rucksacks[0]) {
                if (
                    rucksacks[1].includes(item) &&
                    rucksacks[2].includes(item)
                ) {
                    itemToFind = item;
                    break;
                }
            }

            sum += itemToPriority(itemToFind);
        }

        return sum;
    }
}
