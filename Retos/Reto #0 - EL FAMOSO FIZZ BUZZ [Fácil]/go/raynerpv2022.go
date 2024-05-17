package main

import "fmt"

func main() {
	fmt.Println("FIZZ BUZZ")
	// if condition
	for i := 1; i < 101; i++ {
		if i%3 == 0 && i%5 == 0 {
			fmt.Println("FIZZ BUZZ")
		} else if i%3 == 0 {
			fmt.Println("FIZZ")
		} else if i%5 == 0 {
			fmt.Println("BUZZ")
		} else {
			fmt.Println(i)
		}
	}

}
