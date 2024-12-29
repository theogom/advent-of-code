package main

import (
	utils "advent-of-code/2024/internal"
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

func getDigitCount(n int) int {
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

func naiveBlinkStones(stones []int, blinkCount int) int {
	for i := 0; i < blinkCount; i++ {
		blinkedStones := []int{}

		for _, stone := range stones {
			leftStone, rightStone, splitted := blinkStone(stone)
			blinkedStones = append(blinkedStones, leftStone)

			if splitted {
				blinkedStones = append(blinkedStones, rightStone)
			}
		}

		stones = blinkedStones
	}

	return len(stones)
}

func smartBlinkStones(stones []int, blinkCount int) int {
	blinkedStones := make(map[int]map[int]int)
	stoneCount := 0

	for _, stone := range stones {
		stoneCount += smartBlinkStone(stone, blinkCount, blinkedStones)
	}

	return stoneCount
}

func blinkStone(stone int) (int, int, bool) {
	if stone == 0 {
		return 1, 0, false
	}

	if digitCount := getDigitCount(stone); digitCount%2 == 0 {
		divisor := int(math.Pow10(digitCount / 2))

		return stone / divisor, stone % divisor, true
	}

	return stone * 2024, 0, false
}

func smartBlinkStone(stone int, blinkCount int, blinkedStones map[int]map[int]int) int {
	if blinkCount == 0 {
		return 1
	}

	if blinkedStones[stone][blinkCount] > 0 {
		return blinkedStones[stone][blinkCount]
	}

	leftStone, rightStone, splitted := blinkStone(stone)

	var stoneCount int

	if splitted {
		stoneCount = smartBlinkStone(leftStone, blinkCount-1, blinkedStones) + smartBlinkStone(rightStone, blinkCount-1, blinkedStones)
	} else {
		stoneCount = smartBlinkStone(leftStone, blinkCount-1, blinkedStones)
	}

	if _, ok := blinkedStones[stone]; !ok {
		blinkedStones[stone] = make(map[int]int)
	}

	blinkedStones[stone][blinkCount] = stoneCount

	return stoneCount
}

func partOne(day int) int {
	input := utils.GetInput(day)
	stones := parseStones(input)
	blinkCount := 25

	return naiveBlinkStones(stones, blinkCount)
}

func partTwo(day int) int {
	input := utils.GetInput(day)
	stones := parseStones(input)
	blinkCount := 75

	return smartBlinkStones(stones, blinkCount)
}

func main() {
	utils.Solve(11, partOne, partTwo)
}
