package main

import (
	"bufio"
	"fmt"
	"log"
	"math/big"
	"os"
	"strconv"
	"strings"
)

func main() {
	num := readNumber()
	fmt.Println(checkNumber(num))
}

func readNumber() int {
	fmt.Println("Introduce un número y pulsa enter")
	reader := bufio.NewReader(os.Stdin)

	str, err := reader.ReadString('\n')
	if err != nil {
		log.Fatalf("Fallo al leer el número. Razon: %v", err)
	}

	number, err := strconv.Atoi(strings.TrimRight(str, "\n"))
	if err != nil {
		log.Fatalf("Numero invalido. %v", err)
	}

	return number
}

func checkNumber(number int) string {

	primeText := isPrime(number)
	fiboText := isFibonacci(number)
	parText := isPar(number)
	return fmt.Sprintf("%d %s, %s y %s", number, primeText, fiboText, parText)
}

func isPrime(number int) string {
	if big.NewInt(int64(number)).ProbablyPrime(0) {
		return "es primo"
	}
	return "no es primo"
}

func isFibonacci(number int) string {
	a := 0
	b := 1

	if (number == a) || (number == b) {
		return "fibonacci"
	}
	c := a + b
	for c <= number {
		if c == number {
			return "fibonacci"
		}
		a = b
		b = c
		c = a + b
	}
	return "no es fibonacci"
}

func isPar(number int) string {
	if number%2 == 0 {
		return "es par"
	}
	return "es impar"
}
