package main

import "fmt"

func main() {
	n := 100

	fizzbuzz(n)
}

func fizzbuzz(n int) {
	if n == 0 {
		return
	}
	fizzbuzz(n - 1)

	if n%3 == 0 && n%5 == 0 {
		fmt.Println("fizzbuzz")
	} else if n%3 == 0 {
		fmt.Println("fizz")
	} else if n%5 == 0 {
		fmt.Println("buzz")
	} else {
		fmt.Println(n)
	}
}
