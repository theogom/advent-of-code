package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
)

var mulRegex = regexp.MustCompile(`mul\((\d+),(\d+)\)`)
var doReversedRegex = regexp.MustCompile(`\)\(od`)
var dontReversedRegex = regexp.MustCompile(`\)\(t'nod`)

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

func mul(instruction []string) int {
	return parseInt(instruction[1]) * parseInt(instruction[2])
}

func reverse(s string) string {
	reversed := []rune(s)

	for i, j := 0, len(reversed)-1; i < j; i, j = i+1, j-1 {
		reversed[i], reversed[j] = reversed[j], reversed[i]
	}

	return string(reversed)
}

func partOne(day int) int {
	input := getInput(day)
	regex := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	instructions := regex.FindAllStringSubmatch(input, -1)

	result := 0

	for _, instruction := range instructions {
		result += mul(instruction)
	}

	return result
}

func partTwo(day int) int {
	input := getInput(day)
	reversedInput := reverse(input)

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
	day := 3

	partOne := partOne(day)
	fmt.Printf("Part one: %d\n", partOne)

	partTwo := partTwo(day)
	fmt.Printf("Part two: %d\n", partTwo)
}
