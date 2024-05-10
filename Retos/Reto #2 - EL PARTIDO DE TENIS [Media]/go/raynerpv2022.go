package main

import (
	"fmt"
)

func main() {
	fmt.Println("Tennis GAme")
	p1 := 0
	p2 := 0
	point := map[int]string{0: "LOVE", 1: "15", 2: "30", 3: "40"}
	score := []int{1, 1, 1, 1, 1, 1, 1, 1}

	for _, i := range score {
		if i == 1 {
			p1++
		} else {
			p2++
		}
		if (p1 > 2) && (p1 == p2) {

			fmt.Println("DEUCE")
			continue
		}
		if p1 > 3 {
			if p1-p2 >= 2 {
				fmt.Println("GANA P1")
				break
			}
			if p1-p2 >= 1 {
				fmt.Println("VENTAJA P1")
				continue
			}

		}
		if p2 > 3 {
			if p2-p1 >= 2 {
				fmt.Println("GANA P2")
				break
			}
			if p2-p1 >= 1 {
				fmt.Println("VENTAJA P2")
				continue
			}
		}
		fmt.Println(point[p1], point[p2])
	}

}
