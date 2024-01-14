package main

import (
	"fmt"
	"time"
)

func main() {

	fmt.Printf("Is Friday Thirteen on January 2024? %t \n", checkIfFridayThirteen(2024, 1))
	fmt.Printf("Is Friday Thirteen on September 2024? %t\n", checkIfFridayThirteen(2024, 9))
}

func checkIfFridayThirteen(year, month int) bool {
	d := time.Date(year, time.Month(month), 13, 0, 0, 0, 0, time.Local)
	return d.Weekday() == time.Friday
}
