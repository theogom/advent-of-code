import { DayAbstract } from '../utils/day';

enum Outcome {
    Lose = 0,
    Draw = 3,
    Win = 6,
}

enum ShapeName {
    Rock,
    Paper,
    Scissors,
}

type Shape = {
    name: ShapeName;
    score: number;
    loseAgainst: ShapeName;
    winAgainst: ShapeName;
};

type MoveOpponent = 'A' | 'B' | 'C';

type MoveMe = 'X' | 'Y' | 'Z';

type Game = {
    shapeMe: Shape;
    shapeOpponent: Shape;
};

type OutcomeIdentifier = 'X' | 'Y' | 'Z';

const rock = {
    name: ShapeName.Rock,
    loseAgainst: ShapeName.Paper,
    winAgainst: ShapeName.Scissors,
    score: 1,
};

const paper = {
    name: ShapeName.Paper,
    loseAgainst: ShapeName.Scissors,
    winAgainst: ShapeName.Rock,
    score: 2,
};

const scissors = {
    name: ShapeName.Scissors,
    loseAgainst: ShapeName.Rock,
    winAgainst: ShapeName.Paper,
    score: 3,
};

function getShape(shapeName: ShapeName): Shape {
    switch (shapeName) {
        case ShapeName.Rock:
            return rock;
        case ShapeName.Paper:
            return paper;
        case ShapeName.Scissors:
            return scissors;
    }
}

function opponentToShape(move: MoveOpponent): Shape {
    const mapping = {
        A: ShapeName.Rock,
        B: ShapeName.Paper,
        C: ShapeName.Scissors,
    };

    return getShape(mapping[move]);
}

function meToShape(move: MoveMe): Shape {
    const mapping = {
        X: ShapeName.Rock,
        Y: ShapeName.Paper,
        Z: ShapeName.Scissors,
    };

    return getShape(mapping[move]);
}

function play(shape1: Shape, shape2: Shape): Outcome {
    if (shape1 === shape2) {
        return Outcome.Draw;
    }

    return shape1.loseAgainst === shape2.name ? Outcome.Lose : Outcome.Win;
}

function CharToOutcome(char: OutcomeIdentifier): Outcome {
    const mapping = {
        X: Outcome.Lose,
        Y: Outcome.Draw,
        Z: Outcome.Win,
    };

    return mapping[char];
}

function shouldDo(shape: Shape, outcome: Outcome): Shape {
    switch (outcome) {
        case Outcome.Draw:
            return shape;
        case Outcome.Lose:
            return getShape(shape.winAgainst);
        case Outcome.Win:
            return getShape(shape.loseAgainst);
    }
}

type Input = string[][];

export class Day extends DayAbstract {
    parse(input: string): Input {
        return input.split('\n').map((line) => {
            const chars = line.split(' ');
            return [chars[0], chars[1]];
        });
    }

    partOne() {
        const games: Game[] = this.input.map((chars: string[]) => {
            const [moveOpponent, moveMe]: [MoveOpponent, MoveMe] = chars as [
                MoveOpponent,
                MoveMe
            ];

            return {
                shapeOpponent: opponentToShape(moveOpponent),
                shapeMe: meToShape(moveMe),
            };
        });

        const scores = games.map(
            (game) =>
                play(game.shapeMe, game.shapeOpponent) + game.shapeMe.score
        );

        return scores.reduce((acc, score) => acc + score, 0);
    }

    partTwo() {
        const games: Game[] = this.input.map((chars: string[]) => {
            const [moveOpponent, outcomeIdentifier]: [
                MoveOpponent,
                OutcomeIdentifier
            ] = chars as [MoveOpponent, OutcomeIdentifier];
            const shapeOpponent = opponentToShape(moveOpponent);
            const outcome = CharToOutcome(outcomeIdentifier);
            const shapeMe = shouldDo(shapeOpponent, outcome);

            return {
                shapeOpponent,
                shapeMe,
            };
        });

        const scores = games.map(
            (game) =>
                play(game.shapeMe, game.shapeOpponent) + game.shapeMe.score
        );

        return scores.reduce((acc, score) => acc + score, 0);
    }
}
