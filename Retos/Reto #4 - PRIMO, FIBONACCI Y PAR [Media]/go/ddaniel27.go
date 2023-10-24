package main

import "fmt"

func main() {
	nTest := 13
	response := fmt.Sprintf("%d is ", nTest)
	if isPrime(nTest) {
		response += "prime, "
	} else {
		response += "not prime, "
	}

	if isFibonacci(nTest) {
		response += "fibonacci, "
	} else {
		response += "not fibonacci, "
	}

	if isEven(nTest) {
		response += "even"
	} else {
		response += "odd"
	}

	fmt.Println(response)
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i < n; i++ {
		if (n % i) == 0 {
			return false
		}
	}
	return true
}

func isFibonacci(n int) bool {
	if n <= 1 {
		return true
	}
	a, b := 0, 1
	for a < n {
		a, b = b, a+b
	}
	return a == n
}

func isEven(n int) bool {
	return n%2 == 0
}
