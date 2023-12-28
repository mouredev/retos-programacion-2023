package main

import "fmt"

// definir metodos de trabajo
type Spock interface {
	StartGame()
	PrintScore()
}

const (
	STONE    = "🗿"
	PAPER    = "📄"
	SCISSORS = "✂️"
	LIZZARD  = "🦎"
	SPOCK    = "🖖"
)

// implementar metodos

type Game struct {
	Entrys [][]string
	Result string
}

func (g *Game) StartGame() {
	var (
		p1 int
		p2 int
	)
	for _, entry := range g.Entrys {
		result := BattleGame(entry)
		if result == "player1" {
			p1++
		} else if result == "player2" {
			p2++
		}
	}
	if p1 > p2 {
		g.Result = "Player1"
	} else {
		g.Result = "Player2"
	}
}
func (g Game) PrintScore() {
	fmt.Printf("Entry: %v Result: %v", g.Entrys, g.Result)
}

// funcion auxilar para determinar resultados
func BattleGame(entry []string) string {
	var win string
	combinates := map[string][]string{
		PAPER:    {SCISSORS, LIZZARD},
		STONE:    {PAPER, SPOCK},
		SCISSORS: {STONE, SPOCK},
		LIZZARD:  {STONE, SCISSORS},
		SPOCK:    {LIZZARD, PAPER},
	}
	for g := 0; g < len(entry); g++ {
		for _, val := range combinates[entry[g]] {
			if val == entry[1] {
				win = "player2"
				break
			} else if val == entry[0] {
				win = "player1"
				break
			}
		}
	}
	return win
}

func main() {
	entrys := [][]string{{STONE, SCISSORS}, {SCISSORS, STONE}, {PAPER, SCISSORS}}
	var game Spock = &Game{Entrys: entrys}
	game.StartGame()
	game.PrintScore()
}
