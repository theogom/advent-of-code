package main

import (
	utils "advent-of-code/2024/internal"
)

type HorizontalDirection int
type VerticalDirection int

type Direction struct {
	X HorizontalDirection
	Y VerticalDirection
}

const (
	HorizontalNone HorizontalDirection = iota
	Left
	Right
)

const (
	VerticalNone VerticalDirection = iota
	Up
	Down
)

var Directions = [...]Direction{{Left, Up}, {Left, VerticalNone}, {Left, Down}, {HorizontalNone, Up}, {HorizontalNone, Down}, {Right, Up}, {Right, VerticalNone}, {Right, Down}}

// Move the cursor in the given direction.
func move(position utils.Position, direction Direction) utils.Position {
	switch direction.X {
	case Left:
		position.X--
	case Right:
		position.X++
	}

	switch direction.Y {
	case Up:
		position.Y--
	case Down:
		position.Y++
	}

	return position
}

// Check if the grid contains the given word starting at the given position in the given direction.
func hasWord(grid utils.Grid, word string, position utils.Position, direction Direction) bool {
	if word == "" {
		return true
	}

	if grid.IsOutOfBounds(position) {
		return false
	}

	if rune(grid.GetPoint(position)) != rune(word[0]) {
		return false
	}

	return hasWord(grid, word[1:], move(position, direction), direction)
}

func partOne(day int) int {
	input := utils.GetInput(day)
	grid := utils.ParseGrid(input)

	word := "XMAS"
	wordCount := 0

	for y := range grid.Size {
		for x := range grid.Size {
			for _, direction := range Directions {
				if hasWord(grid, word, utils.Position{X: x, Y: y}, direction) {
					wordCount++
				}
			}
		}
	}

	return wordCount
}

func partTwo(day int) int {
	input := utils.GetInput(day)
	grid := utils.ParseGrid(input)

	word := "MAS"
	wordCount := 0

	for y := range grid.Size {
		for x := range grid.Size {
			cursor := utils.Position{X: x, Y: y}
			if (!hasWord(grid, word, move(cursor, Direction{Left, Up}), Direction{Right, Down}) && !hasWord(grid, word, move(cursor, Direction{Right, Down}), Direction{Left, Up})) {
				continue
			}

			if (!hasWord(grid, word, move(cursor, Direction{Right, Up}), Direction{Left, Down}) && !hasWord(grid, word, move(cursor, Direction{Left, Down}), Direction{Right, Up})) {
				continue
			}

			wordCount++
		}
	}

	return wordCount
}

func main() {
	utils.Solve(4, partOne, partTwo)
}
