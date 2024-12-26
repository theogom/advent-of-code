package utils

import (
	"fmt"
)

func Solve(day int, partOne func(int) int, partTwo func(int) int) {
	fmt.Println("Day", day)
	fmt.Println("=>", partOne(day))
	fmt.Println("=>", partTwo(day))
}
