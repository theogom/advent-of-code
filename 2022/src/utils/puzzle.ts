export abstract class PuzzleAbstract {
    protected input: any;

    constructor(input: string) {
        this.input = this.parse(input);
    }

    abstract parse(input: string): any;
    abstract partOne(): number;
    abstract partTwo(): number;
}
