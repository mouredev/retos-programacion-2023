package main

import (
	"fmt"
	"strings"
)

const rows = 10
const cols = 10

var piece = [][]int{
	{1, 0},
	{1, 1},
	{1, 0},
	{1, 0},
}

var board [rows][cols]int
var pieceRow, pieceCol int

func resetBoard() {
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			board[r][c] = 0
		}
	}
}

func placePiece() {
	pieceRow, pieceCol = 0, 0
	for r := 0; r < len(piece); r++ {
		for c := 0; c < len(piece[r]); c++ {
			board[pieceRow+r][pieceCol+c] = piece[r][c]
		}
	}
}

func moveLeft() {
	if pieceCol > 0 {
		pieceCol--
		updateBoard()
	}
}

func moveRight() {
	if pieceCol+len(piece[0]) < cols {
		pieceCol++
		updateBoard()
	}
}

func moveDown() {
	if pieceRow+len(piece) < rows {
		pieceRow++
		updateBoard()
	}
}

func rotatePiece() {
	newPiece := make([][]int, len(piece[0]))
	for i := range newPiece {
		newPiece[i] = make([]int, len(piece))
	}
	for r := 0; r < len(piece); r++ {
		for c := 0; c < len(piece[r]); c++ {
			newPiece[c][len(piece)-r-1] = piece[r][c]
		}
	}
	if pieceRow+len(newPiece) <= rows && pieceCol+len(newPiece[0]) <= cols {
		piece = newPiece
		updateBoard()
	}
}

func updateBoard() {
	resetBoard()
	for r := 0; r < len(piece); r++ {
		for c := 0; c < len(piece[r]); c++ {
			board[pieceRow+r][pieceCol+c] = piece[r][c]
		}
	}
}

func printBoard() {
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if board[r][c] == 1 {
				fmt.Print("🔳")
			} else {
				fmt.Print("🔲")
			}
		}
		fmt.Println()
	}
}

func main() {
	resetBoard()
	placePiece()

	for {
		printBoard()
		fmt.Println("Enter action (left, right, down, rotate, quit):")
		var action string
		_, err := fmt.Scanln(&action)
		if err != nil {
			return
		}

		switch strings.ToLower(action) {
		case "left":
			moveLeft()
		case "right":
			moveRight()
		case "down":
			moveDown()
		case "rotate":
			rotatePiece()
		case "quit":
			return
		default:
			fmt.Println("Invalid action.")
		}
	}
}
