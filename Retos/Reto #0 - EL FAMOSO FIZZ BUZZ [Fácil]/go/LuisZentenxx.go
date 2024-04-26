package main

import "fmt"

func main() {

	for i := 1; i <= 100; i++ {

		if i%3 == 0 && i%5 == 0 {
			fmt.Println(i, "fizzbuzz")

		} else if i%3 == 0 {
			fmt.Println(i, "fizz")

		} else if i%5 == 0 {
			fmt.Println(i, "buzz")

		} else {
			fmt.Println(i)
		}
	}
}
