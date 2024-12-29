package main

import (
	utils "advent-of-code/2024/internal"
	"fmt"
	"math"
	"strings"
)

func parseStones(input string) []int {
	stones := []int{}

	for _, stone := range strings.Split(input, " ") {
		stones = append(stones, utils.ParseInt(stone))
	}

	return stones
}

func getDigits(n int) int {
	if n == 0 {
		return 1
	}

	if n < 0 {
		n = -n
	}

	count := 0

	for n > 0 {
		n /= 10
		count++
	}

	return count
}

func blink(stones []int) []int {
	blinkedStones := []int{}

	for _, stone := range stones {
		if stone == 0 {
			blinkedStones = append(blinkedStones, 1)
		} else if digits := getDigits(stone); digits%2 == 0 {
			divisor := int(math.Pow10(digits / 2))
			blinkedStones = append(blinkedStones, stone/divisor)
			blinkedStones = append(blinkedStones, stone%divisor)
		} else {
			blinkedStones = append(blinkedStones, stone*2024)
		}
	}

	return blinkedStones
}

func partOne(day int) int {
	input := utils.GetInput(day)
	stones := parseStones(input)
	blinkCount := 10

	for i := 0; i < blinkCount; i++ {
		fmt.Println("blink", i, "len", len(stones))
		stones = blink(stones)
	}

	return len(stones)
}

func partTwo(day int) int {
	input := utils.GetInput(day)
	stones := parseStones(input)
	blinkCount := 0

	for i := 0; i < blinkCount; i++ {
		stones = blink(stones)
		fmt.Println("blink", i)
	}

	return len(stones)
}

func main() {
	utils.Solve(11, partOne, partTwo)
}
