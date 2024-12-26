package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Equation struct {
	Operands []int
	Result   int
}

type Operator = int

const (
	Add Operator = iota
	Mul
	Concat
)

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}

func getInputPath(day int) string {
	return fmt.Sprintf("inputs/input%d.txt", day)
}

func getInput(day int) string {
	filePath := getInputPath(day)
	data, err := os.ReadFile(filePath)

	checkErr(err)

	return string(data)
}

func parseInt(input string) int {
	integer, err := strconv.Atoi(input)

	checkErr(err)

	return integer
}

func parseLines(input string) []string {
	return strings.Split(input, "\n")
}

func parseEquation(input string) Equation {
	elements := strings.Split(input, " ")
	result := parseInt(strings.TrimSuffix(elements[0], ":"))

	operands := make([]int, len(elements)-1)

	for i, operand := range elements[1:] {
		operands[i] = parseInt(operand)
	}

	return Equation{Operands: operands, Result: result}
}

func calculate(operator Operator, firstOperand int, secondOperand int) int {
	switch operator {
	case Add:
		return firstOperand + secondOperand
	case Mul:
		return firstOperand * secondOperand
	case Concat:
		return parseInt(fmt.Sprintf("%d%d", firstOperand, secondOperand))
	}

	panic(fmt.Sprintf("Invalid operator %d", operator))
}

func (equation Equation) solvable(operators []Operator) bool {
	if len(equation.Operands) == 0 {
		return false
	}

	if len(equation.Operands) == 1 {
		return equation.Operands[0] == equation.Result
	}

	for _, operator := range operators {
		operands := append([]int{calculate(operator, equation.Operands[0], equation.Operands[1])}, equation.Operands[2:]...)
		equation := Equation{Operands: operands, Result: equation.Result}

		if equation.solvable(operators) {
			return true
		}
	}

	return false
}

func partOne(day int) int {
	input := getInput(day)
	lines := parseLines(input)
	result := 0

	for _, line := range lines {
		equation := parseEquation(line)

		if equation.solvable([]Operator{Add, Mul}) {
			result += equation.Result
		}
	}

	return result
}

func partTwo(day int) int {
	input := getInput(day)
	lines := parseLines(input)
	result := 0

	for _, line := range lines {
		equation := parseEquation(line)

		if equation.solvable([]Operator{Add, Mul, Concat}) {
			result += equation.Result
		}
	}

	return result
}

func main() {
	day := 7

	partOne := partOne(day)
	fmt.Printf("Part one: %d\n", partOne)

	partTwo := partTwo(day)
	fmt.Printf("Part two: %d\n", partTwo)
}
