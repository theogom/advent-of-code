package utils

import (
	"fmt"
	"strings"
)

type Direction int

type Point rune

type Position struct {
	X, Y int
}

type Grid struct {
	Points [][]Point
	Size   int
}

const (
	NoneDirection Direction = iota
	Up
	Down
	Left
	Right
)

func (direction Direction) String() string {
	switch direction {
	case Up:
		return "Up"
	case Down:
		return "Down"
	case Left:
		return "Left"
	case Right:
		return "Right"
	}

	return ""
}

func (grid Grid) GetPoint(position Position) Point {
	return grid.Points[position.Y][position.X]
}

func (grid Grid) IsOutOfBounds(position Position) bool {
	return position.X < 0 || position.X >= grid.Size || position.Y < 0 || position.Y >= grid.Size
}

func (grid Grid) String() string {
	builder := strings.Builder{}

	for y := 0; y < grid.Size; y++ {
		for x := 0; x < grid.Size; x++ {
			builder.WriteRune(rune(grid.GetPoint(Position{X: x, Y: y})))
		}

		if y < grid.Size-1 {
			builder.WriteString("\n")
		}
	}

	return builder.String()
}

func (point Point) String() string {
	return string(point)
}

// Get the next position in the given direction.
func (position Position) Move(direction Direction) Position {
	switch direction {
	case Left:
		return Position{X: position.X - 1, Y: position.Y}
	case Right:
		return Position{X: position.X + 1, Y: position.Y}
	case Up:
		return Position{X: position.X, Y: position.Y - 1}
	case Down:
		return Position{X: position.X, Y: position.Y + 1}
	}

	panic(fmt.Sprint("Invalid direction", direction))
}

func ParseGrid(input string) Grid {
	lines := ParseLines(input)
	size := len(lines)
	points := make([][]Point, size)

	for y, line := range lines {
		points[y] = make([]Point, size)

		for x, point := range line {
			points[y][x] = Point(point)
		}
	}

	return Grid{Points: points, Size: size}
}
