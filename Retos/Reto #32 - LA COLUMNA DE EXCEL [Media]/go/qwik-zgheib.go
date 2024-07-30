package main

import (
	"fmt"
	"strings"
)

func columnNumber(column string) int {
	result := 0
	length := len(column)
	column = strings.ToUpper(column)

	for i := 0; i < length; i++ {
		result *= 26
		result += int(column[i] - 'A' + 1)
	}

	return result
}

func main() {
	fmt.Println(columnNumber("A"))
	fmt.Println(columnNumber("Z"))
	fmt.Println(columnNumber("AA"))
	fmt.Println(columnNumber("CA"))
	fmt.Println(columnNumber("AAA"))
}
