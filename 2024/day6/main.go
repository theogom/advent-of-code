package main

import (
	"fmt"
	"os"
	"strings"
)

type Point = rune

type Position struct {
	X, Y int
}

type Guard struct {
	Direction        Direction
	Position         Position
	VisitedPositions map[Position]Direction
}

type Size struct {
	Width, Height int
}

type Grid struct {
	Points [][]Point
	Size   Size
}

type Direction int

const (
	GuardPoint    Point = '^'
	EmptyPoint    Point = '.'
	ObstaclePoint Point = '#'
)

const (
	HorizontalNone Direction = iota
	Up
	Down
	Left
	Right
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

func parseLines(input string) []string {
	return strings.Split(input, "\r\n")
}

func parseGrid(input string) (Grid, Guard) {
	lines := parseLines(input)
	size := Size{Height: len(lines)}
	points := make([][]rune, size.Height)

	if len(lines) > 0 {
		size.Width = len(lines[0])
	}

	var position Position

	for y, line := range lines {
		points[y] = make([]rune, len(line))

		for x, point := range line {
			points[y][x] = point

			if point == GuardPoint {
				position = Position{X: x, Y: y}
			}
		}
	}

	return Grid{Points: points, Size: size}, Guard{Direction: Up, Position: position, VisitedPositions: make(map[Position]Direction)}
}

func (grid Grid) GetPoint(position Position) Point {
	return grid.Points[position.Y][position.X]
}

func (grid Grid) AddObstacle(position Position) Grid {
	// Need to create a deep copy of the points
	points := make([][]Point, len(grid.Points))

	for y := range grid.Points {
		points[y] = make([]Point, len(grid.Points[y]))
		copy(points[y], grid.Points[y])
	}

	points[position.Y][position.X] = ObstaclePoint

	return Grid{
		Points: points,
		Size:   grid.Size,
	}
}

func (grid Grid) Show() {
	for y := 0; y < grid.Size.Height; y++ {
		for x := 0; x < grid.Size.Width; x++ {
			fmt.Printf("%c", grid.GetPoint(Position{X: x, Y: y}))
		}

		fmt.Println()
	}
}

func (guard Guard) Copy() Guard {
	// Need to create a deep copy of the visited positions
	visitedPositions := make(map[Position]Direction, len(guard.VisitedPositions))
	for key, value := range guard.VisitedPositions {
		visitedPositions[key] = value
	}

	return Guard{
		Direction:        guard.Direction,
		Position:         guard.Position,
		VisitedPositions: visitedPositions,
	}
}

func (guard Guard) GetNextPosition() Position {
	switch guard.Direction {
	case Up:
		return Position{X: guard.Position.X, Y: guard.Position.Y - 1}
	case Right:
		return Position{X: guard.Position.X + 1, Y: guard.Position.Y}
	case Down:
		return Position{X: guard.Position.X, Y: guard.Position.Y + 1}
	case Left:
		return Position{X: guard.Position.X - 1, Y: guard.Position.Y}
	}

	return guard.Position
}

func (guard Guard) Visited() bool {
	return guard.VisitedPositions[guard.Position] == guard.Direction
}

func (guard *Guard) Move(position Position) {
	guard.Position = position
}

func (guard *Guard) Visit() {
	guard.VisitedPositions[guard.Position] = guard.Direction
}

func (guard *Guard) Rotate() {
	switch guard.Direction {
	case Up:
		guard.Direction = Right
	case Right:
		guard.Direction = Down
	case Down:
		guard.Direction = Left
	case Left:
		guard.Direction = Up
	}
}

func (grid Grid) IsOutOfBounds(position Position) bool {
	return position.X < 0 || position.X >= grid.Size.Width || position.Y < 0 || position.Y >= grid.Size.Height
}

// Visit a grid
// Return true the grid has been exited or false if the guard is in a loop
func (guard *Guard) VisitGrid(grid Grid) bool {
	guard.Visit()

	for !grid.IsOutOfBounds(guard.Position) {
		nextPosition := guard.GetNextPosition()

		if grid.IsOutOfBounds(nextPosition) {
			guard.Move(nextPosition)
			continue
		}

		nextPoint := grid.GetPoint(nextPosition)

		if nextPoint == ObstaclePoint {
			guard.Rotate()
			continue
		}

		guard.Move(nextPosition)

		// Stuck in a loop
		if guard.Visited() {
			return false
		}

		guard.Visit()

	}

	return true
}

func partOne(day int) int {
	input := getInput(day)
	grid, guard := parseGrid(input)

	guard.VisitGrid(grid)

	return len(guard.VisitedPositions)
}

func partTwo(day int) int {
	input := getInput(day)
	grid, guard := parseGrid(input)
	possibleObstructionCount := 0

	for y := 0; y < grid.Size.Height; y++ {
		for x := 0; x < grid.Size.Width; x++ {
			position := Position{X: x, Y: y}

			if grid.GetPoint(position) != EmptyPoint {
				continue
			}

			obstructedGrid := grid.AddObstacle(position)
			copiedGuard := guard.Copy()

			if !copiedGuard.VisitGrid(obstructedGrid) {
				possibleObstructionCount++
			}
		}
	}

	return possibleObstructionCount
}

func main() {
	day := 6

	partOne := partOne(day)
	fmt.Printf("Part one: %d\n", partOne)

	partTwo := partTwo(day)
	fmt.Printf("Part two: %d\n", partTwo)
}
