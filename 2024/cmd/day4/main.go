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

type Grid struct {
	Letters []string
	Width   int
	Height  int
}

type Point struct {
	X int
	Y int
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

func parseGrid(input string) Grid {
	letters := utils.ParseLines(input)

	height := len(letters)

	if height == 0 {
		return Grid{letters, 0, 0}
	}

	width := len(letters[0])

	return Grid{letters, width, height}
}

// Check if a point is in the bound of the grid
func isInBounds(grid Grid, point Point) bool {
	return point.X >= 0 && point.X < grid.Width && point.Y >= 0 && point.Y < grid.Height
}

// Move the cursor in the given direction.
func move(cursor Point, direction Direction) Point {
	switch direction.X {
	case Left:
		cursor.X--
	case Right:
		cursor.X++
	}

	switch direction.Y {
	case Up:
		cursor.Y--
	case Down:
		cursor.Y++
	}

	return cursor
}

// Check if the grid contains the given word starting at the given point in the given direction.
func hasWord(grid Grid, word string, cursor Point, direction Direction) bool {
	if word == "" {
		return true
	}

	if !isInBounds(grid, cursor) {
		return false
	}

	if grid.Letters[cursor.X][cursor.Y] != word[0] {
		return false
	}

	return hasWord(grid, word[1:], move(cursor, direction), direction)
}

func partOne(day int) int {
	input := utils.GetInput(day)
	grid := parseGrid(input)

	word := "XMAS"
	wordCount := 0

	for y := range grid.Height {
		for x := range grid.Width {
			for _, direction := range Directions {
				if hasWord(grid, word, Point{x, y}, direction) {
					wordCount++
				}
			}
		}
	}

	return wordCount
}

func partTwo(day int) int {
	input := utils.GetInput(day)
	grid := parseGrid(input)

	word := "MAS"
	wordCount := 0

	for y := range grid.Height {
		for x := range grid.Width {
			cursor := Point{x, y}
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
