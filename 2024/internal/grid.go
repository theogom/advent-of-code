package utils

import "fmt"

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
	Up Direction = iota
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

func (point Point) String() string {
	return string(point)
}

// Get the next position in the given direction.
func (position Position) Next(direction Direction) Position {
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
