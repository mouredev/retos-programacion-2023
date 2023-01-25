package main

import (
	"fmt"
	"strconv"
)

func isEvenNumber(number int) string {
	if number%2 == 0 {
		return "es par y "
	}
	return "no es par y "
}

func isPrimeNumber(number int) string {
	if number < 2 {
		return "no es primo, "
	}
	for i := 2; i < number; i++ {
		if number%i == 0 {
			return "no es primo, "
		}
	}
	return "es primo, "
}

func isFibonacciNumber(number int) string {
	a := 0
	b := 1
	for a < number {
		a, b = b, a+b
	}
	if a == number {
		return "es un numero de Fibonacci"
	}
	return "no es un numero de Fibonacci"
}

func CheckNumber(number int) string {
	var isPrime string = isPrimeNumber(number)
	var isFibonacci string = isFibonacciNumber(number)
	var isEven string = isEvenNumber(number)

	return "El numero " + strconv.Itoa(number) + " " + isPrime + isEven + isFibonacci
}

func main() {
	fmt.Println(CheckNumber(1))
	fmt.Println(CheckNumber(2))
	fmt.Println(CheckNumber(3))
	fmt.Println(CheckNumber(4))
	fmt.Println(CheckNumber(5))
	fmt.Println(CheckNumber(6))
	fmt.Println(CheckNumber(7))
	fmt.Println(CheckNumber(8))
	fmt.Println(CheckNumber(9))
	fmt.Println(CheckNumber(10))
	fmt.Println(CheckNumber(1024))
	fmt.Println(CheckNumber(358742586))

}
