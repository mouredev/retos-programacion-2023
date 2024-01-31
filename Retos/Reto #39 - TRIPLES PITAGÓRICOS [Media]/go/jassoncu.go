package main

import (
	"fmt"
)

func findPythagoreanTriples(max int) [][]int {
	var triples [][]int

	for a := 1; a <= max; a++ {
		for b := a + 1; b <= max; b++ {
			c := int(1.0 + (float64(a*a) + float64(b*b))) // Calcular la hipotenusa c

			// Verificar si es un triple pitagórico
			if c <= max && c*c == a*a+b*b {
				triples = append(triples, []int{a, b, c})
			}
		}
	}

	return triples
}

func main() {
	// Ejemplo de uso
	max := 19
	result := findPythagoreanTriples(max)

	if len(result) > 0 {
		fmt.Printf("Triples pitagóricos menores o iguales a %d: %v\n", max, result)
	} else {
		fmt.Printf("No hay triples pitagóricos menores o iguales a %d\n", max)
	}
}
