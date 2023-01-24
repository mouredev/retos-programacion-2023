package main

import (
	"fmt"
	"log"
	"math"
)

func isEven(num int) bool {
	return num%2 == 0
}

func isPrime(num int) bool {
	if num == 2 {
		return true
	}

	if num <= 1 || isEven(num) {
		return false
	}

	for i := 3; i <= int(math.Sqrt(float64(num))); i += 2 {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func isPerfecSquare(num int) bool {
	var square int = int(math.Sqrt(float64(num)))
	return num == square*square
}

func isFibonacci(num int) bool {
	if num < 0 {
		return false
	}
	return isPerfecSquare(5*num*num+4) || isPerfecSquare(5*num*num-4)
}

func evaluateNumber(num int) string {
	var notPrime, notFibon, evenOrOdd string

	if !isPrime(num) {
		notPrime = "no "
	}

	if !isFibonacci(num) {
		notFibon = "no "
	}

	if isEven(num) {
		evenOrOdd = "par"
	} else {
		evenOrOdd = "impar"
	}

	return fmt.Sprintf("%d %ses primo, %ses fibonacci y es %s", num, notPrime, notFibon, evenOrOdd)
}

func main() {
	tests := []struct {
		num  int
		want string
	}{
		{-29, "-29 no es primo, no es fibonacci y es impar"},
		{-1, "-1 no es primo, no es fibonacci y es impar"},
		{0, "0 no es primo, es fibonacci y es par"},
		{2, "2 es primo, es fibonacci y es par"},
		{3, "3 es primo, es fibonacci y es impar"},
		{5, "5 es primo, es fibonacci y es impar"},
		{8, "8 no es primo, es fibonacci y es par"},
		{107, "107 es primo, no es fibonacci y es impar"},
		{144, "144 no es primo, es fibonacci y es par"},
		{854, "854 no es primo, no es fibonacci y es par"},
	}

	for _, test := range tests {
		got := evaluateNumber(test.num)

		if got != test.want {
			log.Printf("Test failed:\n\tnum: %d\n\tgot: %q\n\twant: %q\n\n", test.num, got, test.want)
		}
	}
}
