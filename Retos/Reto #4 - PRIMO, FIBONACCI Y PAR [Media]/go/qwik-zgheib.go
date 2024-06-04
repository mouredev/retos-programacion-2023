package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type PrimeChecker interface {
	IsPrime(n int) bool
}

type FibonacciChecker interface {
	IsFibonacci(n int) bool
}

type EvenChecker interface {
	IsEven(n int) bool
}

type NumberChecker struct{}

func NewNumberChecker() *NumberChecker {
	return &NumberChecker{}
}

func (nc *NumberChecker) IsPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func (nc *NumberChecker) IsFibonacci(n int) bool {
	if n == 0 || n == 1 {
		return true
	}
	a, b := 0, 1
	for b < n {
		a, b = b, a+b
	}
	return b == n
}

func (nc *NumberChecker) IsEven(n int) bool {
	return n%2 == 0
}

func getInput(prompt string) string {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(prompt)
	input, _ := reader.ReadString('\n')
	return strings.TrimSpace(input)
}

func main() {
	var n int
	var err error

	for {
		input := getInput("Enter a number: ")
		n, err = strconv.Atoi(input)
		if err == nil {
			break
		}
		fmt.Println("Invalid input. Please enter a valid number.")
	}

	nc := NewNumberChecker()

	isPrime := nc.IsPrime(n)
	isFibonacci := nc.IsFibonacci(n)
	isEven := nc.IsEven(n)

	result := fmt.Sprintf("%d is", n)

	if isPrime {
		result += " prime,"
	} else {
		result += " it's not prime,"
	}

	if isFibonacci {
		result += " fibonacci"
	} else {
		result += " not fibonacci"
	}

	if isEven {
		result += " and even."
	} else {
		result += " and odd."
	}

	fmt.Println(result)
}
