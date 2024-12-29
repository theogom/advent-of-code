package main

import (
	utils "advent-of-code/2024/internal"
)

type Guard struct {
	Direction        utils.Direction
	Position         utils.Position
	VisitedPositions map[utils.Position]utils.Direction
}

const (
	GuardPoint    utils.Point = '^'
	EmptyPoint    utils.Point = '.'
	ObstaclePoint utils.Point = '#'
)

func getGuard(grid utils.Grid) Guard {
	for y := 0; y < grid.Size; y++ {
		for x := 0; x < grid.Size; x++ {
			position := utils.Position{X: x, Y: y}
			point := grid.GetPoint(position)

			if point == GuardPoint {
				return Guard{Direction: utils.Up, Position: position, VisitedPositions: make(map[utils.Position]utils.Direction)}
			}
		}
	}

	panic("no guard found")
}

func addObstacle(grid utils.Grid, position utils.Position) utils.Grid {
	// Need to create a deep copy of the points
	points := make([][]utils.Point, grid.Size)

	for y := range grid.Points {
		points[y] = make([]utils.Point, len(grid.Points[y]))
		copy(points[y], grid.Points[y])
	}

	points[position.Y][position.X] = ObstaclePoint

	return utils.Grid{
		Points: points,
		Size:   grid.Size,
	}
}

func (guard Guard) Copy() Guard {
	// Need to create a deep copy of the visited positions
	visitedPositions := make(map[utils.Position]utils.Direction, len(guard.VisitedPositions))
	for key, value := range guard.VisitedPositions {
		visitedPositions[key] = value
	}

	return Guard{
		Direction:        guard.Direction,
		Position:         guard.Position,
		VisitedPositions: visitedPositions,
	}
}

func (guard Guard) Visited() bool {
	return guard.VisitedPositions[guard.Position] == guard.Direction
}

func (guard *Guard) Move(position utils.Position) {
	guard.Position = position
}

func (guard *Guard) Visit() {
	guard.VisitedPositions[guard.Position] = guard.Direction
}

func (guard *Guard) Rotate() {
	switch guard.Direction {
	case utils.Up:
		guard.Direction = utils.Right
	case utils.Right:
		guard.Direction = utils.Down
	case utils.Down:
		guard.Direction = utils.Left
	case utils.Left:
		guard.Direction = utils.Up
	}
}

// Visit a grid
// Return true the grid has been exited or false if the guard is in a loop
func (guard *Guard) VisitGrid(grid utils.Grid) bool {
	guard.Visit()

	for !grid.IsOutOfBounds(guard.Position) {
		nextPosition := guard.Position.Move(guard.Direction)

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
	input := utils.GetInput(day)
	grid := utils.ParseGrid(input)
	guard := getGuard(grid)

	guard.VisitGrid(grid)

	return len(guard.VisitedPositions)
}

func partTwo(day int) int {
	input := utils.GetInput(day)
	grid := utils.ParseGrid(input)
	guard := getGuard(grid)

	possibleObstructionCount := 0

	for y := 0; y < grid.Size; y++ {
		for x := 0; x < grid.Size; x++ {
			position := utils.Position{X: x, Y: y}

			if grid.GetPoint(position) != EmptyPoint {
				continue
			}

			obstructedGrid := addObstacle(grid, position)
			copiedGuard := guard.Copy()

			if !copiedGuard.VisitGrid(obstructedGrid) {
				possibleObstructionCount++
			}
		}
	}

	return possibleObstructionCount
}

func main() {
	utils.Solve(6, partOne, partTwo)
}
