package main

import (
	"fmt"
	"strings"
)

type SpiralDrawer interface {
	DrawSpiral(size int) [][]rune
}

type Printer interface {
	Print(matrix [][]rune)
}

type SimpleSpiralDrawer struct{}

func NewSimpleSpiralDrawer() *SimpleSpiralDrawer {
	return &SimpleSpiralDrawer{}
}

func (sd *SimpleSpiralDrawer) DrawSpiral(size int) [][]rune {
	matrix := make([][]rune, size)
	for i := range matrix {
		matrix[i] = make([]rune, size)
	}

	for row := 0; row < size; row++ {
		horizontal := row == 0
		for col := 0; col < size; col++ {
			switch {
			case row+col == size-1:
				if col >= row {
					matrix[row][col] = '╗'
				} else {
					matrix[row][col] = '╚'
				}
				horizontal = col < row
			case row-col == 1 && row < size/2:
				matrix[row][col] = '╔'
				horizontal = true
			case row == col && row >= size/2:
				matrix[row][col] = '╝'
				horizontal = false
			default:
				if horizontal {
					matrix[row][col] = '═'
				} else {
					matrix[row][col] = '║'
				}
			}
		}
	}
	return matrix
}

type SimplePrinter struct{}

func NewSimplePrinter() *SimplePrinter {
	return &SimplePrinter{}
}

func (sp *SimplePrinter) Print(matrix [][]rune) {
	for _, row := range matrix {
		fmt.Println(strings.TrimSpace(string(row)))
	}
}

func main() {
	spiralDrawer := NewSimpleSpiralDrawer()
	printer := NewSimplePrinter()

	size := 5
	spiral := spiralDrawer.DrawSpiral(size)
	printer.Print(spiral)
}
