package main

import (
	"fmt"
	"time"
)

func random() int64 {
	return time.Now().UnixNano() % 101
}

func main() {
	for i := 0; i < 10; i++ {
		fmt.Println("Random number:", random())
	}
}
