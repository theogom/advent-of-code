package main

import (
	utils "advent-of-code/2024/internal"
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

func getLineFunction(firstPosition, secondPosition Position) func(int) Position {
	if firstPosition.X == secondPosition.X {
		// Works because the definition domain of x is the same as the y one
		return func(x int) Position {
			return Position{X: firstPosition.X, Y: x}
		}
	}

	if firstPosition.Y == secondPosition.Y {
		return func(x int) Position {
			return Position{X: x, Y: firstPosition.Y}
		}
	}

	xCoefficient := utils.Abs(secondPosition.Y - firstPosition.Y)
	yCoefficient := utils.Abs(secondPosition.X - firstPosition.X)
	yIntercept := float32(firstPosition.Y) - float32(slope*float32(firstPosition.X))

	fmt.Println(firstPosition, secondPosition)
	fmt.Printf("f(y) = %fx + %f\n", slope, yIntercept)

	return func(x int) Position {
		return Position{X: x, Y: int(slope*float32(x) + yIntercept)}
	}
}

// Get the lined antinodes of two antennas
// Lined antinode is a point in line with the two antennas
func getLinedAntinodes(size int, firstAntenna, secondAntenna Position) []Position {
	lineFunction := getLineFunction(firstAntenna, secondAntenna)
	antinodes := []Position{}

	for x := 0; x < size; x++ {
		antinodes = append(antinodes, lineFunction(x))
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
				grid.Show()
			}
		}
	}

	return len(antinodes)
}

func main() {
	utils.Solve(8, partOne, partTwo)
}
