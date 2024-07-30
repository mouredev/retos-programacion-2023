package main

import (
	"fmt"
)

func main() {
	var number int

	fmt.Print("enter a number: ")
	_, err := fmt.Scan(&number)
	if err != nil {
		return
	}

	fmt.Printf("multiplication table %d:\n", number)
	for i := 1; i <= 10; i++ {
		result := number * i
		fmt.Printf("%d x %d = %d\n", number, i, result)
	}
}
