package main

import (
	"fmt"
	"strings"
)

func readAbacus(abacus []string) int {
	number := 0
	multiplier := 1_000_000

	for _, row := range abacus {
		parts := strings.Split(row, "---")
		leftSide := len(parts[0])
		number += leftSide * multiplier
		multiplier /= 10
	}

	return number
}

func main() {
	abacus := []string{
		"O---OOOOOOOO",
		"OOO---OOOOOO",
		"---OOOOOOOOO",
		"OO---OOOOOOO",
		"OOOOOOO---OO",
		"OOOOOOOOO---",
		"---OOOOOOOOO",
	}

	result := readAbacus(abacus)
	fmt.Printf("Resultado: %d\n", result)
}
