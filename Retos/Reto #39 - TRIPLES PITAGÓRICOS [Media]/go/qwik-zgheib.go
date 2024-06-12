package main

import (
	"fmt"
)

func findPythagoreanTriples(max int) [][3]int {
	var triples [][3]int

	for a := 1; a <= max; a++ {
		for b := a; b <= max; b++ {
			for c := b; c <= max; c++ {
				if a*a+b*b == c*c {
					triples = append(triples, [3]int{a, b, c})
				}
			}
		}
	}

	return triples
}

func main() {
	var maxValue int
	fmt.Print("enter a max number: ")
	_, err := fmt.Scan(&maxValue)
	if err != nil {
		return
	}

	triples := findPythagoreanTriples(maxValue)

	fmt.Printf("pythagorean triples less than or equal to %d:\n", maxValue)
	for _, triple := range triples {
		fmt.Printf("(%d, %d, %d)\n", triple[0], triple[1], triple[2])
	}
}
