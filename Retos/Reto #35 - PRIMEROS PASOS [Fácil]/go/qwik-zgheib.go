package main

import (
	"errors"
	"fmt"
)

func main() {
	// Hello, World!
	fmt.Println("Hello, World!")

	// Create variables of different types
	var str string = "I am a string"
	var integer int = 42
	var decimal float64 = 3.14
	var boolean bool = true

	fmt.Println(str, integer, decimal, boolean)

	// Create a constant
	const constant string = "I am a constant"
	fmt.Println(constant)

	// Use if, else if, and else
	if integer < 20 {
		fmt.Println("The integer is less than 20")
	} else if integer == 42 {
		fmt.Println("The integer is 42")
	} else {
		fmt.Println("The integer is greater than 20")
	}

	// Create structures
	// Array
	var array [3]int = [3]int{1, 2, 3}
	fmt.Println(array)

	// Slice (similar to a list)
	var slice []int = []int{1, 2, 3, 4, 5}
	fmt.Println(slice)

	// Map (similar to a dictionary)
	var dictionary map[string]int = map[string]int{"one": 1, "two": 2}
	fmt.Println(dictionary)

	// Use for, foreach, and while
	// Traditional for loop
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	// Foreach using range
	for index, value := range slice {
		fmt.Printf("Index: %d, Value: %d\n", index, value)
	}

	// While loop (in Go, this is done with for)
	j := 0
	for j < 5 {
		fmt.Println(j)
		j++
	}

	// Different functions
	noParamsNoReturn()
	withParamsNoReturn("Hello from function with parameters")
	result := noParamsWithReturn()
	fmt.Println(result)
	sum := withParamsWithReturn(5, 7)
	fmt.Println(sum)

	// Creating a class (struct in Go)
	type Person struct {
		name string
		age  int
	}

	// Creating an object
	person := Person{name: "Qwik", age: 22}
	fmt.Println(person)

	// Exception handling
	divisionResult, err := divide(10, 0)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Division result:", divisionResult)
	}
}

// Function without parameters and without return
func noParamsNoReturn() {
	fmt.Println("Function without parameters and without return")
}

// Function with parameters and without return
func withParamsNoReturn(message string) {
	fmt.Println(message)
}

// Function without parameters and with return
func noParamsWithReturn() string {
	return "Return from function without parameters"
}

// Function with parameters and with return
func withParamsWithReturn(a int, b int) int {
	return a + b
}

// Function that handles exceptions (errors in Go)
func divide(a int, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("cannot divide by zero")
	}
	return a / b, nil
}
