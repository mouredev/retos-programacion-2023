package main

import (
	"fmt"
	"strconv"
	"time"
)

func friday13(month int, year int) bool {

	date := time.Date(year, time.Month(month), 13, 0, 0, 0, 0, time.UTC)

	return date.Weekday() == time.Friday
}

func main() {

	for {
		// Ask user to enter month and year
		var monthStr, yearStr string
		fmt.Print("Enter month (1-12): ")
		fmt.Scanln(&monthStr)
		fmt.Print("Enter year (ej. 2023): ")
		fmt.Scanln(&yearStr)

		// Convert strings to int
		m, err1 := strconv.Atoi(monthStr)
		y, err2 := strconv.Atoi(yearStr)

		// Handle conversion errors
		if err1 != nil || err2 != nil {
			fmt.Println("Error: You mut enter numeric values")
			continue
		}

		result := friday13(m, y)
		fmt.Println(result)
		break
	}

}
