package utils

import "strconv"

func ParseInt(input string) int {
	integer, err := strconv.Atoi(input)

	CheckError(err)

	return integer
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}

	return x
}
