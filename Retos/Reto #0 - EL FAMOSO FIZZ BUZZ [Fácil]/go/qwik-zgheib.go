package main

import (
	"fmt"
)

func main() {
	printFizzBuzzRecursive(1, 100)
}

// printFizzBuzzRecursive is a recursive function that prints the FizzBuzz sequence from the given start to end.
//
// Parameters:
// - current: The current number in the sequence.
// - end: The last number in the sequence.
//
// Return:
// - This function does not return any value. It prints the FizzBuzz sequence to the console.
func printFizzBuzzRecursive(current, end int) {
	if current > end {
		return
	}
	fmt.Println(fizzBuzz(current))
	printFizzBuzzRecursive(current+1, end)
}

// fizzBuzz is a helper function that returns the FizzBuzz string for a given number.
//
// Parameters:
// - n: The number to check.
//
// Return:
// - A string representing the FizzBuzz value for the given number.
//   - If n is divisible by both 3 and 5, it returns "fizzbuzz".
//   - If n is divisible by 3, it returns "fizz".
//   - If n is divisible by 5, it returns "buzz".
//   - If n is not divisible by 3 or 5, it returns the number as a string.
func fizzBuzz(n int) string {
	if n%3 == 0 && n%5 == 0 {
		return "fizzbuzz"
	} else if n%3 == 0 {
		return "fizz"
	} else if n%5 == 0 {
		return "buzz"
	} else {
		return fmt.Sprintf("%d", n)
	}
}
