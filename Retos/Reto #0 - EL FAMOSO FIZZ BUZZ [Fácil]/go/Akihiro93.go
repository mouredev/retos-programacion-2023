package main

import (
	"fmt"
)

func frizz_buzz(n int) {
	if n%3 == 0 && n%5 == 0 {
		fmt.Println("frizzbuzz")
	} else if n%3 == 0 {
		fmt.Println("frizz")
	} else if n%5 == 0 {
		fmt.Println("buzz")
	} else {
		fmt.Println(n)
	}
}

func main() {
	for i := 1; i <= 100; i++ {
		frizz_buzz(i)
	}
}
