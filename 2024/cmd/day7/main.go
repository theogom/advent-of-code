package main

import (
	utils "advent-of-code/2024/internal"
	"fmt"
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

func parseEquation(input string) Equation {
	elements := strings.Split(input, " ")
	result := utils.ParseInt(strings.TrimSuffix(elements[0], ":"))

	operands := make([]int, len(elements)-1)

	for i, operand := range elements[1:] {
		operands[i] = utils.ParseInt(operand)
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
		return utils.ParseInt(fmt.Sprintf("%d%d", firstOperand, secondOperand))
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
	input := utils.GetInput(day)
	lines := utils.ParseLines(input)
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
	input := utils.GetInput(day)
	lines := utils.ParseLines(input)
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
	utils.Solve(7, partOne, partTwo)
}
