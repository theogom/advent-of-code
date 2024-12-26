package main

import (
	utils "advent-of-code/2024/internal"
	"regexp"
)

var mulRegex = regexp.MustCompile(`mul\((\d+),(\d+)\)`)
var doReversedRegex = regexp.MustCompile(`\)\(od`)
var dontReversedRegex = regexp.MustCompile(`\)\(t'nod`)

func mul(instruction []string) int {
	return utils.ParseInt(instruction[1]) * utils.ParseInt(instruction[2])
}

func partOne(day int) int {
	input := utils.GetInput(day)
	regex := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	instructions := regex.FindAllStringSubmatch(input, -1)

	result := 0

	for _, instruction := range instructions {
		result += mul(instruction)
	}

	return result
}

func partTwo(day int) int {
	input := utils.GetInput(day)
	reversedInput := utils.Reverse(input)

	cursor := 0
	var reversedCursor int

	result := 0

	for {
		mulIndex := mulRegex.FindStringIndex(input[cursor:])

		if mulIndex == nil {
			break
		}

		reversedCursor = len(input) - 1 - cursor - mulIndex[1]

		if reversedCursor < 0 {
			break
		}

		doIndex := doReversedRegex.FindStringIndex(reversedInput[reversedCursor:])
		dontIndex := dontReversedRegex.FindStringIndex(reversedInput[reversedCursor:])

		if dontIndex == nil || (doIndex != nil && doIndex[0] < dontIndex[0]) {
			instruction := mulRegex.FindStringSubmatch(input[cursor:])

			if instruction != nil {
				result += mul(instruction)
			}
		}

		cursor += mulIndex[1]
	}

	return result
}

func main() {
	utils.Solve(3, partOne, partTwo)
}
