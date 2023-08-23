package main

import (
	"fmt"
	"time"
)

func countdown(start int, seconds int) {
	for start > 0 {
		fmt.Println(start)
		time.Sleep(time.Duration(seconds) * time.Second)
		start--
	}

	fmt.Println("¡Cuenta atrás finalizada!")
}

func main() {
	start := 10
	seconds := 1

	countdown(start, seconds)
}
