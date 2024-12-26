package utils

import (
	"fmt"
	"os"
)

func getInputPath(day int) string {
	return fmt.Sprintf("inputs/input%d.txt", day)
}

func GetInput(day int) string {
	filePath := getInputPath(day)
	data, err := os.ReadFile(filePath)

	CheckError(err)

	return string(data)
}
