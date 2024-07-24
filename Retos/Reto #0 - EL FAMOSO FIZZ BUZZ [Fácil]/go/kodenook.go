package main

import (
	"fmt"
	"strings"
	"time"
)

// The main function in Go generates a sequence of numbers and prints "fizz" for multiples of 3, "buzz"
// for multiples of 5, and the number itself if neither, displaying the execution time at the end.
func main() {
	start := time.Now()

	for i:=0; i<=100;i++ {
		var output strings.Builder

		if i%3 == 0 {
			_, _ = output.WriteString("fizz")
		}
		if i%5 == 0 {
			_, _ = output.WriteString("buzz")
		}

		if output.String() == "" {
			_, _ = output.WriteString(fmt.Sprintf("%v", i))
		}

		fmt.Println(output.String())

	}

	duration := time.Since(start)
	fmt.Printf("\nExecution time: %v\n", duration)
}