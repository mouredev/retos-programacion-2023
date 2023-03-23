package main

import "fmt"

func main() {
	for i := 1; i <= 100; i++ {
		var output string

		if i%3 == 0 {
			output += "fizz"
		}

		if i%5 == 0 {
			output += "buzz"
		}

		if output != "" {
			fmt.Println(output)
		} else {
			fmt.Println(i)
		}
	}
}
