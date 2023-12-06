package main

import (
	"fmt"
	"time"
)

func isFriday13(month, year int) bool {
	input := fmt.Sprintf("%d-%02d-%02d", year, month, 13)
	date, err := time.Parse("2006-01-02", input)

	if err != nil {
		return false
	}

	return date.Weekday() == time.Friday
}

func main() {
	month, year := 1, 2023
	result := isFriday13(month, year)
	fmt.Println(result)
}
