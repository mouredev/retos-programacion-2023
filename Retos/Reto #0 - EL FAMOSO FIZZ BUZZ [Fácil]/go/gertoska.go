package main

import "fmt"

const MaxNumber int8 = 100

func main() {
	var i int8 = 1

	for ; i <= MaxNumber; i++ {
		if isMultiple(i, 3) && isMultiple(i, 5) {
			output("fizzbuzz")
		} else if isMultiple(i, 3) {
			output("fizz")
		} else if isMultiple(i, 5) {
			output("buzz")
		} else {
			output(i)
		}
	}
}

// Check if the number is a multiple. Returns true or false.
func isMultiple(number int8, multiple int8) bool {
	return number%multiple == 0
}

// Returns a result. In this case with the Println function
func output(intOrStringVariable interface{}) {
	fmt.Println(intOrStringVariable)
}

