package main

import (
	utils "advent-of-code/2024/internal"
)

const (
	TrailheadPoint utils.Point = '0'
	TerminusPoint  utils.Point = '9'
)

func getTrailheads(grid utils.Grid) []utils.Position {
	trailheads := []utils.Position{}

	for y := 0; y < grid.Size; y++ {
		for x := 0; x < grid.Size; x++ {
			position := utils.Position{X: x, Y: y}
			if grid.GetPoint(position) == TrailheadPoint {
				trailheads = append(trailheads, position)
			}
		}
	}

	return trailheads
}

func getTrailheadScore(grid utils.Grid, trailhead utils.Position) int {
	return len(findTerminuses(grid, trailhead))
}

func getTrailheadRating(grid utils.Grid, trailhead utils.Position) int {
	trailheadRating := 0

	for _, terminusRating := range findTerminuses(grid, trailhead) {
		trailheadRating += terminusRating
	}

	return trailheadRating
}

func findTerminuses(grid utils.Grid, position utils.Position) map[utils.Position]int {
	directions := [4]utils.Direction{utils.Up, utils.Down, utils.Left, utils.Right}
	currentPoint := grid.GetPoint(position)
	terminuses := make(map[utils.Position]int)

	for _, direction := range directions {
		nextPosition := position.Move(direction)

		if grid.IsOutOfBounds(nextPosition) {
			continue
		}

		nextPoint := grid.GetPoint(nextPosition)

		if nextPoint != currentPoint+1 {
			continue
		}

		if nextPoint == TerminusPoint {
			terminuses[nextPosition]++
			continue
		}

		for terminus, rating := range findTerminuses(grid, nextPosition) {
			terminuses[terminus] += rating
		}
	}

	return terminuses
}

func partOne(day int) int {
	input := utils.GetInput(day)
	grid := utils.ParseGrid(input)

	score := 0

	for _, trailhead := range getTrailheads(grid) {
		score += getTrailheadScore(grid, trailhead)
	}

	return score
}

func partTwo(day int) int {
	input := utils.GetInput(day)
	grid := utils.ParseGrid(input)

	rating := 0

	for _, trailhead := range getTrailheads(grid) {
		rating += getTrailheadRating(grid, trailhead)
	}

	return rating
}

func main() {
	utils.Solve(10, partOne, partTwo)
}
