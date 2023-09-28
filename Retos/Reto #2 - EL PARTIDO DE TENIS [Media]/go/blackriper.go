package main

import "fmt"

// definimos metodos de trabajo
type Tenis interface {
	PlayTenis()
}

// implementar metodos de trabajo
type Player struct {
	Sequence []string
}

func (p *Player) PlayTenis() {
	player1 := 0
	player2 := 0

	for _, turn := range p.Sequence {
		if turn == "P1" {
			player1++
		} else if turn == "P2" {
			player2++
		}
		if player1 == 4 && player2 == 4 {
			player1 = 3
			player2 = 3
		}
		PrintResults(player1, player2)
	}
}

// funcion auxilar para imprimir resultados
func PrintResults(p1, p2 int) {
	score := []string{"Love", "15", "30", "40"}
	switch {
	case p1 == p2 && p1 == 3:
		fmt.Println("Deuce")
	case p1 == 4 && p2 == 3:
		fmt.Println("Advantage P1")
	case p2 == 4 && p1 == 3:
		fmt.Println("Advantage P2")
	case p1 == 5 && (p1-p2) == 2:
		fmt.Println("Was won P1")
	case p2 == 5 && (p2-p1) == 2:
		fmt.Println("Was won P2")
	default:
		fmt.Printf("%v - %v\n ", score[p1], score[p2])
	}
}

func main() {
	sequence := []string{"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"}
	var tenis Tenis = &Player{Sequence: sequence}
	tenis.PlayTenis()
}
