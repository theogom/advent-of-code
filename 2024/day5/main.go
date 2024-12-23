package main

import (
	"fmt"
	"os"
	"slices"
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

func parseInput(input string) ([]string, []string) {
	sections := strings.Split(input, "\r\n\r\n")

	return parseLines(sections[0]), parseLines(sections[1])
}

// Parse the order section
// @param An list of order as pipe separated integers
// @return A map of pages mapped with the pages that should come before
func parseOrders(rawOrders []string) map[string][]string {
	orders := make(map[string][]string, len(rawOrders))

	for _, rawOrder := range rawOrders {
		order := strings.Split(rawOrder, "|")
		orders[order[0]] = append(orders[order[0]], order[1])
	}

	return orders
}

// Parse a line of the update section
// @param An update as comma separated integers
// @return The list of update
func parseUpdate(rawUpdate string) []string {
	return strings.Split(rawUpdate, ",")
}

func parseInt(input string) int {
	integer, err := strconv.Atoi(input)

	checkErr(err)

	return integer
}

func parseLines(input string) []string {
	return strings.Split(input, "\r\n")
}

func getComparePages(orders map[string][]string) func(a string, b string) int {
	return func(pageA string, pageB string) int {
		if slices.Contains(orders[pageA], pageB) {
			return -1
		}

		return 1
	}
}

func sortPages(pages []string, orders map[string][]string) []string {
	for pageIndex, page := range pages {
		nextPages := orders[page]

		if len(nextPages) == 0 {
			continue
		}

		for previousPageIndex, previousPage := range pages[:pageIndex] {
			if slices.Contains(nextPages, previousPage) {
				pages = slices.Delete(pages, previousPageIndex, previousPageIndex+1)
				pages = slices.Insert(pages, pageIndex, previousPage)
				return sortPages(pages, orders)
			}
		}
	}

	return pages
}

func getMiddlePage(pages []string) int {
	return parseInt(pages[len(pages)/2])
}

func partOne(day int) int {
	input := getInput(day)
	rawOrders, rawUpdates := parseInput(input)
	orders := parseOrders(rawOrders)

	isSorted := getComparePages(orders)

	result := 0

	for _, rawUpdate := range rawUpdates {
		pages := parseUpdate(rawUpdate)

		if slices.IsSortedFunc(pages, isSorted) {
			result += getMiddlePage(pages)
		}
	}

	return result
}

func partTwo(day int) int {
	input := getInput(day)
	rawOrders, rawUpdates := parseInput(input)
	orders := parseOrders(rawOrders)
	isSorted := getComparePages(orders)

	result := 0

	for _, rawUpdate := range rawUpdates {
		pages := parseUpdate(rawUpdate)

		if !slices.IsSortedFunc(pages, isSorted) {
			orderedPages := sortPages(pages, orders)
			result += getMiddlePage(orderedPages)
		}
	}

	return result
}

func main() {
	day := 5

	partOne := partOne(day)
	fmt.Printf("Part one: %d\n", partOne)

	partTwo := partTwo(day)
	fmt.Printf("Part two: %d\n", partTwo)
}
