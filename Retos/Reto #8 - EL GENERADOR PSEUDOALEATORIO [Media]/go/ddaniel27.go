package main

import "time"

const MAXINT64 = 9223372036854775807

func main() {
	seed := time.Now().UnixNano()
	var x int64 = 1

	for i := 0; i < 10; i++ {
		if x == 0 {
			x = 1
		}
		x = (((MAXINT64 + seed) / x) + x) / 2
		x = x % 137
		if x == 0 {
			x = 1
		}
		x = (((MAXINT64 + seed) / x) + x) / 2
		x = x % 100
	}

	println(x)
}
