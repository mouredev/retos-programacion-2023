package main

import "fmt"

func main() {
	for i := 1; i <= 100; i++ {
		if i%3 != 0 && i%5 != 0 {
			fmt.Println(i)
			continue
		}

		if i%5 != 0 {
			fmt.Println("fizz")
			continue
		}

		if i%3 != 0 {
			fmt.Println("buzz")
			continue
		}

		fmt.Println("fizzbuzz")
	}
}
