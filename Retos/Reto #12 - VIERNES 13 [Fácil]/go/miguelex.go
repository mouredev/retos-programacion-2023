package main

import (
	"fmt"
	"time"
)

func isFridaythe13th(month int, year int) bool {
	date := time.Date(year, time.Month(month), 13, 0, 0, 0, 0, time.UTC)
	return date.Weekday() == time.Friday
}

func main() {
	fmt.Println("¿Hay viernes 13 en marzo de 2023?", isFridaythe13th(3, 2023))
	fmt.Println("¿Hay viernes 13 en octubre de 2023?", isFridaythe13th(10, 2023))
}
