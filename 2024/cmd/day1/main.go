package main

import (
	utils "advent-of-code/2024/internal"
	"slices"
	"strings"
)

func parseIds(input string) ([]int, []int) {
	lines := utils.ParseLines(input)
	pairCount := len(lines)
	leftItems := make([]int, pairCount)
	rightItems := make([]int, pairCount)

	for i, line := range lines {
		pair := strings.Split(line, "   ")
		leftItems[i] = utils.ParseInt(pair[0])
		rightItems[i] = utils.ParseInt(pair[1])
	}

	return leftItems, rightItems
}

func getItemsCount(items []int) map[int]int {
	counts := make(map[int]int)

	for _, item := range items {
		counts[item]++
	}

	return counts
}

func partOne(day int) int {
	input := utils.GetInput(day)
	leftIds, rightIds := parseIds(input)

	slices.Sort(rightIds)
	slices.Sort(rightIds)

	difference := 0

	for i := 0; i < len(leftIds); i++ {
		difference += utils.Abs(leftIds[i] - rightIds[i])
	}

	return difference
}

func partTwo(day int) int {
	input := utils.GetInput(day)
	leftIds, rightIds := parseIds(input)

	idsCount := getItemsCount(rightIds)

	score := 0

	for _, id := range leftIds {
		score += id * idsCount[id]
	}

	return score
}

func main() {
	utils.Solve(1, partOne, partTwo)
}
