/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

package main

import (
	"fmt"
)

func main() {
	for i := range make([]int8, 100) {
		valueNumber := i + 1
		valueString := ""

		if valueNumber%3 == 0 {
			valueString += "Fizz"
		}

		if valueNumber%5 == 0 {
			valueString += "Buzz"
		}

		if valueString == "" {
			fmt.Println(valueNumber)
		} else {
			fmt.Println(valueString)
		}
	}
}
