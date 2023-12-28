/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
 */

package main

import (
	"fmt"
	"strings"
)

func decodeAbacus(abacus []string) int {
	total := 0
	multiplier := 1

	for i := len(abacus) - 1; i >= 0; i-- {
		count := strings.Count(abacus[i], "O")

		if count > 0 {
			total += count * multiplier
		}

		multiplier *= 10
	}

	return total
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

	number := decodeAbacus(abacus)
	fmt.Printf("Resultado: %d\n", number)
}
