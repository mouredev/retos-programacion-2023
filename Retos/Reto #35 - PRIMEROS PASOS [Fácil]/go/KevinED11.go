package main

import (
	"errors"
	"fmt"
)

// Hello world
func helloWorld() {
	fmt.Println("hello world")
}

// Variables
func showVariables() {
	name := "kevin"
	var lastName string = "asael"
	var married bool = true
	var age int8 = 22
	var moneyInTheBank float64 = 1.0

	fmt.Println(name, lastName, married, age, moneyInTheBank)
}

// Constants
func showConstants() {
	const PI = 3.1416
	fmt.Println(PI)
}

// Conditionals
func fizzBuzz(number int) {
	for i := 1; i <= number; i++ {
		if i%15 == 0 {
			// Múltiplo de 3 y 5
			fmt.Println("FizzBuzz")
		} else if i%3 == 0 {
			// Múltiplo de 3
			fmt.Println("Fizz")
		} else if i%5 == 0 {
			// Múltiplo de 5
			fmt.Println("Buzz")
		} else {
			// Ninguno de los anteriores, así que imprime el número mismo
			fmt.Println(i)
		}
	}
}

// Class
type Person struct {
	name string
	age  int8
}

func (p *Person) greet() {
	fmt.Printf("hello %s", p.name)
}

// Structures
type Book struct {
	title, price interface{}
}

func showStructures() {
	// Slice
	numbers := []int{1, 2, 3, 4, 5}

	// Tuple emulation
	book1 := Book{"Harry Potter 1", 15.7}
	book2 := Book{"Lord of the Rings", 17.1}
	book3 := Book{"Gone Girl", 24.8}

	// Array
	heroes := [10]string{"Batman", "SpiderMan"}

	// Map
	account := map[string]int{
		"kevin": 100,
		"juan":  200,
	}

	fmt.Println(numbers, book1, book2, book3, heroes, account)

}

// Loops
func showLoops() {
	counter := 1
	for counter <= 10 {
		fmt.Println(counter)
		counter++
	}

	for _, element := range []string{"kevin", "juan", "alvaro"} {
		fmt.Println(element)
	}
}

// Functions
func isEven(number int) bool {
	return number%2 == 0
}
func greet(name string) {
	fmt.Printf("hello %s", name)
}

func hello() {
	fmt.Println("¡Hello!")
}

// Exceptions
func division(n, n2 int) (int, error) {
	if n2 == 0 {
		return 0, errors.New("la division por zero no es posible")
	}
	return n / n2, nil
}

func main() {

	if r, err := division(10, 0); err != nil {
		println(err)
	} else {
		fmt.Println(r)
	}
}
