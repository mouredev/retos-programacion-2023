package main

import "fmt"

// funcion para saber multiplos de un numero
func MultipleOfaNumber(number int) {
	switch {
	case number%5 == 0 && number%3 == 0:
		fmt.Println("fizzbuzz")
	case number%3 == 0:
		fmt.Println("fizz")
	case number%5 == 0:
		fmt.Println("buzz")
	default:
		fmt.Println(number)
	}
}

func main() {
	for n := 0; n < 100; n++ {
		MultipleOfaNumber(n)
	}
}
