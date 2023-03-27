package main

import (
	"time"
)

// isFriday13 returns true if the given month and year has a Friday 13th
func isFriday13(month, year int) bool {
	return time.Date(year, time.Month(month), 13, 0, 0, 0, 0, time.UTC).Weekday() == time.Friday
}

// Test
func main() {
	month, year := 1, 2023
	result := isFriday13(month, year)
	println(month, year, result)

	month, year = 3, 2020
	result = isFriday13(month, year)
	println(month, year, result)

	month, year = 1, 1985
	result = isFriday13(month, year)
	println(month, year, result)

	month, year = 10, 2015
	result = isFriday13(month, year)
	println(month, year, result)

}
