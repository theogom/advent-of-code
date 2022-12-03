import { readFileSync } from 'fs';
import * as puzzles from './puzzles';

const INPUTS_PATH = __dirname + '/../inputs';

const arg = process.argv?.[2] ?? null;

function printPuzzleHeader(index: number) {
    console.log(`--- Puzzle ${index} ---`);
}

function printError(error: unknown) {
    if (error instanceof Error) {
        console.error('Error:', error.message);
    }
    else {
        console.error('Error', error);
    }
}

function run(index: number) {
    const puzzlePath = `puzzle${index}` as keyof typeof puzzles;
    const inputPath = `input${index}.txt`;
    let input;

    if (!(puzzlePath in puzzles)) {
        throw new Error(`Puzzle ${index} not found, available puzzles: ${Object.keys(puzzles).map(key => key.replace('puzzle', '')).join(', ')}`);
    }

    try {
        input = readFileSync(`${INPUTS_PATH}/${inputPath}`, 'utf-8');
    }
    catch(error) {
        throw new Error(`Input file ${inputPath} not found in inputs directory.`);
    }

    const puzzle = new puzzles[puzzlePath].Puzzle(input);

    console.log(puzzle.partOne());
    console.log(puzzle.partTwo());
}

function runAll() {
    if (Object.keys(puzzles).length === 0) {
        console.log('No puzzles found.');
        return;
    }

    for (let index = 1; index <= Object.keys(puzzles).length; index++) {
        printPuzzleHeader(index);

        try {
            run(index);
        }
        catch(error) {
            printError(error);
        }

        console.log('');
    }
}

if (arg) {
    const index = Number(arg);

    if (isNaN(index)) {
        console.error(`Invalid puzzle index: ${arg}, expected a number`);
        process.exit(1);
    }

    printPuzzleHeader(index);

    try {
        run(index);
    }
    catch (error) {
        printError(error);
        process.exit(1);
    }
}
else {
    runAll();
}