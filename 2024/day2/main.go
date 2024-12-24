package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
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

func abs(x int) int {
	if x < 0 {
		return -x
	}

	return x
}

func parseInt(input string) int {
	integer, err := strconv.Atoi(input)

	checkErr(err)

	return integer
}

func remove(slice []int, removedIndex int) []int {
	sliceCopy := make([]int, len(slice)-1)
	sliceCopyIndex := 0

	for sliceIndex, value := range slice {
		if sliceIndex == removedIndex {
			continue
		}

		sliceCopy[sliceCopyIndex] = value
		sliceCopyIndex++
	}

	return sliceCopy
}

func parseReport(input string) []int {
	levels := strings.Split(input, " ")
	report := make([]int, len(levels))

	for i, level := range levels {
		report[i] = parseInt(level)
	}

	return report
}

func isReportSafeWithError(report []int, toleratedErrorCount int, errorIndex int) bool {
	if toleratedErrorCount == 0 {
		return false
	}

	// Removing the first level can change the order direction
	if errorIndex == 1 && isReportSafe(remove(report, errorIndex-1), toleratedErrorCount-1) {
		return true
	}

	return isReportSafe(remove(report, errorIndex), toleratedErrorCount-1) || isReportSafe(remove(report, errorIndex+1), toleratedErrorCount-1)
}

func isReportSafe(report []int, toleratedErrorCount int) bool {
	if len(report) < 2 {
		return true
	}

	increasing := report[0] < report[1]

	for i := 0; i < len(report)-1; i++ {
		if increasing && report[i] >= report[i+1] {
			return isReportSafeWithError(report, toleratedErrorCount, i)
		} else if !increasing && report[i] <= report[i+1] {
			return isReportSafeWithError(report, toleratedErrorCount, i)
		}

		difference := abs(report[i] - report[i+1])

		if difference < 1 || difference > 3 {
			return isReportSafeWithError(report, toleratedErrorCount, i)
		}
	}

	return true
}

func partOne(day int) int {
	input := getInput(day)
	lines := strings.Split(input, "\r\n")
	safeReportCount := 0

	for _, line := range lines {
		report := parseReport(line)

		if isReportSafe(report, 0) {
			safeReportCount++
		}
	}

	return safeReportCount
}

func partTwo(day int) int {
	input := getInput(day)
	lines := strings.Split(input, "\r\n")
	safeReportCount := 0

	for _, line := range lines {
		report := parseReport(line)

		if isReportSafe(report, 1) {
			safeReportCount++
		}
	}

	return safeReportCount
}

func main() {
	day := 2

	partOne := partOne(day)
	fmt.Printf("Part one: %d\n", partOne)

	partTwo := partTwo(day)
	fmt.Printf("Part two: %d\n", partTwo)
}
