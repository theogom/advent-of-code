export abstract class DayAbstract {
    input: any;

    constructor(input: string) {
        this.input = this.parse(input);
    }

    abstract parse(input: string): any;
    abstract partOne(): number | string;
    abstract partTwo(): number | string;
}
