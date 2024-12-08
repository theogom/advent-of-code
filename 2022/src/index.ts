import { readFileSync } from 'fs';
import * as days from './days';

const INPUTS_PATH = __dirname + '/../inputs';

const arg = process.argv?.[2] ?? null;

function printDayHeader(index: number) {
    console.log(`--- Day ${index} ---`);
}

function printError(error: unknown) {
    if (error instanceof Error) {
        console.error('Error:', error.message);
    } else {
        console.error('Error', error);
    }
}

function run(index: number) {
    const dayPath = `day${index}` as keyof typeof days;
    const inputPath = `input${index}.txt`;
    let input;

    if (!(dayPath in days)) {
        throw new Error(
            `Day ${index} not found, available days: ${Object.keys(days)
                .map((key) => key.replace('day', ''))
                .join(', ')}`
        );
    }

    try {
        input = readFileSync(`${INPUTS_PATH}/${inputPath}`, 'utf-8');
    } catch (error) {
        throw new Error(
            `Input file ${inputPath} not found in inputs directory.`
        );
    }

    const day = new days[dayPath].Day(input);

    console.log(day.partOne());
    console.log(day.partTwo());
}

function runAll() {
    if (Object.keys(days).length === 0) {
        console.log('No days found.');
        return;
    }

    for (let index = 1; index <= Object.keys(days).length; index++) {
        printDayHeader(index);

        try {
            run(index);
        } catch (error) {
            printError(error);
        }

        console.log('');
    }
}

if (arg) {
    const index = Number(arg);

    if (isNaN(index)) {
        console.error(`Invalid day index: ${arg}, expected a number`);
        process.exit(1);
    }

    printDayHeader(index);

    try {
        run(index);
    } catch (error) {
        printError(error);
        process.exit(1);
    }
} else {
    runAll();
}
