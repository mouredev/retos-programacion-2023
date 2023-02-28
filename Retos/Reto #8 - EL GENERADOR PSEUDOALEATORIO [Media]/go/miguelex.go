package main

import (
	"fmt"
	"time"
)

var seed = int(time.Now().UnixNano() / int64(time.Millisecond))

func RadomNumber(a int, m int) int {
	var q = int(m / a)
	var r = int(q % a)

	seed = a*(seed%q) - r*int(seed/q)

	if seed <= 0 {
		seed += m
	}

	return seed
}

func main() {
	fmt.Print("¿Cuantos numeros quieres generar? ")
	var n int
	fmt.Scan(&n)

	var a = int(time.Now().UnixNano() / int64(time.Millisecond))
	var m = int(time.Now().UnixNano()/int64(time.Millisecond)) * 1000

	for i := 0; i < n; i++ {
		fmt.Println(RadomNumber(a, m) % 100)
		time.Sleep(3 * time.Second)
	}
}
