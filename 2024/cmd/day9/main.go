package main

import (
	utils "advent-of-code/2024/internal"
)

const EmptyBlock = -1

func toDisk(diskMap string) []int {
	disk := []int{}
	isFile := true
	fileId := 0

	for _, code := range diskMap {
		var block int

		if isFile {
			block = fileId
			fileId++
		} else {
			block = EmptyBlock
		}

		for i := 0; i < utils.ParseInt(string(code)); i++ {
			disk = append(disk, block)
		}

		isFile = !isFile
	}

	return disk
}

func compactBlocks(disk []int) []int {
	leftCursor := 0
	rightCursor := len(disk) - 1
	emptyBlockFound := false
	fileBlockFound := false

	for leftCursor < rightCursor {
		if emptyBlockFound && fileBlockFound {
			disk[leftCursor] = disk[rightCursor]
			disk[rightCursor] = EmptyBlock
			emptyBlockFound = false
			fileBlockFound = false
		}

		if disk[leftCursor] == EmptyBlock {
			emptyBlockFound = true
		} else {
			leftCursor++
		}

		if disk[rightCursor] != EmptyBlock {
			fileBlockFound = true
		} else {
			rightCursor--
		}
	}

	return disk
}

func getChecksum(disk []int) int {
	checksum := 0

	for i := 0; i < len(disk) && disk[i] != EmptyBlock; i++ {
		checksum += disk[i] * i
	}

	return checksum
}

func partOne(day int) int {
	diskMap := utils.GetInput(day)

	disk := toDisk(diskMap)
	compactedDisk := compactBlocks(disk)
	checksum := getChecksum(compactedDisk)

	return checksum
}

func partTwo(day int) int {
	diskMap := utils.GetInput(day)

	disk := toDisk(diskMap)
	compactedDisk := compactBlocks(disk)
	checksum := getChecksum(compactedDisk)

	return checksum
}

func main() {
	utils.Solve(9, partOne, partTwo)
}
