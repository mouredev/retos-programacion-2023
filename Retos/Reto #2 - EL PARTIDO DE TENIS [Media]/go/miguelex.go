package main

import (
	"fmt"
	"strings"
)

func main() {
	TennisMatch([]string{"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"})
	TennisMatch([]string{"P1", "P1", "P1", "P2", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2"})
}

func TennisMatch(players []string) {
	p1Points := 0
	p2Points := 0
	var i int

	for i = 0; i < len(players); i++ {
		if strings.ToUpper(players[i]) == "P1" {
			p1Points++
		} else if strings.ToUpper(players[i]) == "P2" {
			p2Points++
		} else {
			fmt.Println("Tanteo incorrecto")
		}

		if p1Points == 4 && p2Points == 4 {
			p1Points = 3
			p2Points = 3
		}

		PrintScore(p1Points, p2Points)
	}
}

func PrintScore(P1 int, P2 int) {

	score := []string{"Love", "15", "30", "40"}

	if P1 == P2 && P1 == 3 {
		fmt.Println("\tDeuce")
	} else if P1 == 4 && P2 == 3 {
		fmt.Println("\tVentaja P1")
	} else if P2 == 4 && P1 == 3 {
		fmt.Println("\tVentaja P2")
	} else if P1 == 5 && P1-P2 == 2 {
		fmt.Println("\tGana P1")
	} else if P2 == 5 && P2-P1 == 2 {
		fmt.Println("\tGana P2")
	} else {
		fmt.Println("P1:\t", score[P1], "-", score[P2], "\t:P2")
	}
}
