package main

import (
	"fmt"
)

func main() {
	list := make([]int8, 100)

	for i := range list {
		valueNumber := i + 1
		valueString := ""

		if valueNumber%3 == 0 {
			valueString += "Fizz"
		}

		if valueNumber%5 == 0 {
			valueString += "Buzz"
		}

		if valueString == "" {
			fmt.Println(valueNumber)
		} else {
			fmt.Println(valueString)
		}
	}
}
