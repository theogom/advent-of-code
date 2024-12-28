package main

import (
	utils "advent-of-code/2024/internal"
	"fmt"
)

const FreeBlock = -1

type Disk []int

func toDisk(diskMap string) Disk {
	disk := []int{}
	isFile := true
	fileId := 0

	for _, code := range diskMap {
		var block int

		if isFile {
			block = fileId
			fileId++
		} else {
			block = FreeBlock
		}

		for i := 0; i < utils.ParseInt(string(code)); i++ {
			disk = append(disk, block)
		}

		isFile = !isFile
	}

	return disk
}

func (disk Disk) CompactBlocks() Disk {
	leftCursor := 0
	rightCursor := len(disk) - 1
	emptyBlockFound := false
	fileBlockFound := false

	for leftCursor < rightCursor {
		if emptyBlockFound && fileBlockFound {
			disk[leftCursor] = disk[rightCursor]
			disk[rightCursor] = FreeBlock
			emptyBlockFound = false
			fileBlockFound = false
		}

		if disk[leftCursor] == FreeBlock {
			emptyBlockFound = true
		} else {
			leftCursor++
		}

		if disk[rightCursor] != FreeBlock {
			fileBlockFound = true
		} else {
			rightCursor--
		}
	}

	return disk
}

func (disk Disk) CompactFiles() Disk {
	cursor := len(disk) - 1

	for cursor >= 0 {
		fileEndIndex := disk.FindFile(cursor)

		if fileEndIndex == -1 {
			break
		}

		fileSize := disk.GetFileSize(fileEndIndex)
		fileStartIndex := fileEndIndex - fileSize + 1
		freeSpaceStartIndex := disk.FindFreeSpace(fileSize, fileEndIndex)

		if freeSpaceStartIndex != -1 {
			disk = disk.MoveFile(fileStartIndex, freeSpaceStartIndex, fileSize)
		}

		cursor = fileStartIndex - 1
	}

	return disk
}

func (disk Disk) GetChecksum() int {
	checksum := 0

	for i := 0; i < len(disk); i++ {
		if disk[i] != FreeBlock {
			checksum += disk[i] * i
		}
	}

	return checksum
}

// Get the file size given its end index
func (disk Disk) GetFileSize(endIndex int) int {
	block := disk[endIndex]
	size := 0

	for endIndex >= 0 && endIndex < len(disk) && disk[endIndex] == block {
		size++
		endIndex--
	}

	return size
}

// Find the rightmost file up to the given index
func (disk Disk) FindFile(maxIndex int) int {
	for i := maxIndex; i >= 0; i-- {
		if disk[i] != FreeBlock {
			return i
		}
	}

	return -1
}

func (disk Disk) FindFreeSpace(fileSize, maxIndex int) int {
	freeSpaceSize := 0
	freeSpaceIndex := -1

	for i := 0; i < maxIndex; i++ {
		if disk[i] != FreeBlock {
			freeSpaceSize = 0
			freeSpaceIndex = i + 1
		} else {
			freeSpaceSize++
		}

		if freeSpaceSize == fileSize {
			return freeSpaceIndex
		}
	}

	return -1
}

func (disk Disk) MoveFile(sourceIndex, destinationIndex, size int) Disk {
	block := disk[sourceIndex]

	for i := 0; i < size; i++ {
		disk[sourceIndex+i] = FreeBlock
		disk[destinationIndex+i] = block
	}

	return disk
}

func (disk Disk) Dump() {
	for i := 0; i < len(disk); i++ {
		if disk[i] == FreeBlock {
			fmt.Print(".")
		} else {
			fmt.Print(disk[i])
		}
	}

	fmt.Println()
}

func partOne(day int) int {
	diskMap := utils.GetInput(day)

	disk := toDisk(diskMap)
	compactedDisk := disk.CompactBlocks()
	checksum := compactedDisk.GetChecksum()

	return checksum
}

func partTwo(day int) int {
	diskMap := utils.GetInput(day)

	disk := toDisk(diskMap)
	compactedDisk := disk.CompactFiles()
	checksum := compactedDisk.GetChecksum()

	return checksum
}

func main() {
	utils.Solve(9, partOne, partTwo)
}
