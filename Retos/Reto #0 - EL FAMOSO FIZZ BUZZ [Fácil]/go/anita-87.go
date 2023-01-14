package main

import "fmt"

func main() {
	for i := 0; i <= 100; i++ {
		if i%3 == 0 && i%5 == 0 {
			fmt.Println("fizzbuzz")
			continue
		}
		if i%3 == 0 {
			fmt.Println("fizz")
			continue
		}
		if i%5 == 0 {
			fmt.Println("buzz")
			continue
		}
		fmt.Println(i)
	}
}
