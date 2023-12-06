package main

import "fmt"

func main() {

	for i := 1; i < 101; i++ {
		if (i%3 == 0) && (i%5 == 0) {
			fmt.Println("fizzbuzz")
		} else if i%3 == 0 {
			fmt.Println("fizz")
		} else if i%5 == 0 {
			fmt.Println("buzz")
		} else {
			fmt.Println(i)
		}
	}

}
