package main

import (
	"fmt"

	"github.com/go-vgo/robotgo"
)

func main() {
	generateRamdonNumber()
}

func generateRamdonNumber() {

	x, y := robotgo.GetMousePos()
	fmt.Println((int64(x) * int64(y)) / 100000)

}
