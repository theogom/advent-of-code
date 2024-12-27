package main

import (
	utils "advent-of-code/2024/internal"
	"errors"
	"fmt"
)

type Direction = int
type Point = rune

type Grid struct {
	Size   int
	Points [][]Point
	// Antennas by frequencies
	Antennas map[Point][]Position
}

type Position struct {
	X, Y int
}

const (
	EmptyPoint    Point = '.'
	AntinodePoint Point = '#'
)

const (
	Horizontal Direction = iota
	Vertical
	Diagonal
)

func (grid Grid) IsOutOfBounds(position Position) bool {
	return position.X < 0 || position.X >= grid.Size || position.Y < 0 || position.Y >= grid.Size
}

func (grid Grid) GetPoint(position Position) Point {
	return grid.Points[position.Y][position.X]
}

func (grid Grid) Show() {
	for y := 0; y < grid.Size; y++ {
		for x := 0; x < grid.Size; x++ {
			fmt.Printf("%c", grid.GetPoint(Position{X: x, Y: y}))
		}

		fmt.Println()
	}
}

func (grid *Grid) SetPoint(position Position, point Point) {
	grid.Points[position.Y][position.X] = point
}

func parseGrid(input string) Grid {
	lines := utils.ParseLines(input)
	size := len(lines)
	points := make([][]rune, size)
	antennas := make(map[rune][]Position)

	for y, line := range lines {
		points[y] = make([]rune, len(line))

		for x, point := range line {
			points[y][x] = point

			if point != EmptyPoint {
				antennas[point] = append(antennas[point], Position{x, y})
			}
		}
	}

	return Grid{Size: size, Points: points, Antennas: antennas}
}

// Get the dual antinodes of two antennas
// Dual antinode is a point in line with the two antennas and where one of the antennas is twice as far away as the other
func getDualAntinodes(firstAntenna, secondAntenna Position) [2]Position {
	dx := secondAntenna.X - firstAntenna.X
	dy := secondAntenna.Y - firstAntenna.Y

	return [2]Position{
		{
			X: firstAntenna.X - dx,
			Y: firstAntenna.Y - dy,
		},
		{
			X: secondAntenna.X + dx,
			Y: secondAntenna.Y + dy,
		},
	}
}

func getLineFunction(firstPosition, secondPosition Position) func(int) (Position, error) {
	if firstPosition.X == secondPosition.X {
		// Works because the definition domain of x is the same as the y one
		return func(x int) (Position, error) {
			return Position{X: firstPosition.X, Y: x}, nil
		}
	}

	if firstPosition.Y == secondPosition.Y {
		return func(x int) (Position, error) {
			return Position{X: x, Y: firstPosition.Y}, nil
		}
	}

	xSlope := secondPosition.X - firstPosition.X
	ySlope := secondPosition.Y - firstPosition.Y

	return func(x int) (Position, error) {
		numerator := ySlope*x - ySlope*firstPosition.X

		// Check if y will be defined on the grid (i.e. an integer)
		if numerator%xSlope != 0 {
			return Position{}, errors.New("undefined point")
		}

		return Position{X: x, Y: numerator/xSlope + firstPosition.Y}, nil
	}
}

// Get the lined antinodes of two antennas
// Lined antinode is a point in line with the two antennas
func getLinedAntinodes(size int, firstAntenna, secondAntenna Position) []Position {
	lineFunction := getLineFunction(secondAntenna, firstAntenna)
	antinodes := []Position{}

	for x := 0; x < size; x++ {
		antinode, err := lineFunction(x)

		if err == nil {
			antinodes = append(antinodes, antinode)
		}
	}

	return antinodes
}

func partOne(day int) int {
	input := utils.GetInput(day)

	grid := parseGrid(input)
	antinodes := make(map[Position]struct{})

	for _, antennas := range grid.Antennas {
		for i, firstAntenna := range antennas {
			for _, secondAntenna := range antennas[i+1:] {
				for _, antinode := range getDualAntinodes(firstAntenna, secondAntenna) {
					if !grid.IsOutOfBounds(antinode) {
						grid.SetPoint(antinode, AntinodePoint)
						antinodes[antinode] = struct{}{}
					}
				}
			}
		}
	}

	return len(antinodes)
}

func partTwo(day int) int {
	input := utils.GetInput(day)

	grid := parseGrid(input)
	antinodes := make(map[Position]struct{})

	for _, antennas := range grid.Antennas {
		for i, firstAntenna := range antennas {
			for _, secondAntenna := range antennas[i+1:] {
				for _, antinode := range getLinedAntinodes(grid.Size, firstAntenna, secondAntenna) {
					if !grid.IsOutOfBounds(antinode) {
						grid.SetPoint(antinode, AntinodePoint)
						antinodes[antinode] = struct{}{}
					}
				}
			}
		}
	}

	return len(antinodes)
}

func main() {
	utils.Solve(8, partOne, partTwo)
}
