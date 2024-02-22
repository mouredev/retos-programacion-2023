package main

import (
	"fmt"
)

func main() {
	var number int
	fmt.Print("Introduce un numero: ")
	fmt.Scanf("%d", &number)

	for i := 1; i < 11; i++ {
		result := number * i
		fmt.Println(number ," x ", i, " = ", result)
	}
}