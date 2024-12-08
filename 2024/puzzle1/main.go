package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
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

func parseInput(input string) ([]int, []int) {
	lines := strings.Split(input, "\r\n")
	pairCount := len(lines)
	leftItems := make([]int, pairCount)
	rightItems := make([]int, pairCount)

	for i, line := range lines {
		pair := strings.Split(line, "   ")
		leftItems[i] = parseInt(pair[0])
		rightItems[i] = parseInt(pair[1])
	}

	return leftItems, rightItems
}

func abs(x int) int {
	if x < 0 {
		return -x
	}

	return x
}

func parseInt(s string) int {
	integer, err := strconv.Atoi(s)

	checkErr(err)

	return integer
}

func getItemsCount(items []int) map[int]int {
	counts := make(map[int]int)

	for _, item := range items {
		counts[item] += 1
	}

	return counts
}

func partOne(day int) int {
	input := getInput(day)
	leftIds, rightIds := parseInput(input)

	slices.Sort(rightIds)
	slices.Sort(rightIds)

	difference := 0

	for i := 0; i < len(leftIds); i++ {
		difference += abs(leftIds[i] - rightIds[i])
	}

	return difference
}

func partTwo(day int) int {
	input := getInput(day)
	leftIds, rightIds := parseInput(input)

	idsCount := getItemsCount(rightIds)

	score := 0

	for _, id := range leftIds {
		score += id * idsCount[id]
	}

	return score
}

func main() {
	day := 1

	partOne := partOne(day)
	fmt.Printf("Part one: %d\n", partOne)

	partTwo := partTwo(day)
	fmt.Printf("Part two: %d\n", partTwo)
}
