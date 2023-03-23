package main

import (
	"fmt"
)

/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

func Returnfizzbuzz(num int) string {

	if multiploCinco(num) && multiploTres(num) {
		return "fizzbuzz"
	}

	if multiploTres(num) {
		return "fizz"
	}

	if multiploCinco(num) {
		return "buzz"
	}

	return ""
}

func multiploTres(num int) bool {
	if num%3 != 0 {
		return false
	}
	return true
}

func multiploCinco(num int) bool {
	if num%5 != 0 {
		return false
	}
	return true
}

func main() {
	for i := 1; i <= 100; i++ {
		fmt.Println("para", i, Returnfizzbuzz(i))
	}
}
