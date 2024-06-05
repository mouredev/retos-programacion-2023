package main

import (
	"fmt"
)

type Move string

const (
	Rock     Move = "🗿"
	Paper    Move = "📄"
	Scissors Move = "✂️"
	Lizard   Move = "🦎"
	Spock    Move = "🖖"
)

type Rules interface {
	GetWinner(move1, move2 Move) int
}

type GameRules struct{}

func NewGameRules() *GameRules {
	return &GameRules{}
}

func (gr *GameRules) GetWinner(move1, move2 Move) int {
	if move1 == move2 {
		return 0
	}

	wins := map[Move][]Move{
		Rock:     {Scissors, Lizard},
		Paper:    {Rock, Spock},
		Scissors: {Paper, Lizard},
		Lizard:   {Paper, Spock},
		Spock:    {Rock, Scissors},
	}

	for _, move := range wins[move1] {
		if move == move2 {
			return 1
		}
	}
	return 2
}

type Game struct {
	rules Rules
}

func NewGame(rules Rules) *Game {
	return &Game{rules: rules}
}

func (g *Game) CalculateWinner(moves [][2]Move) string {
	player1Wins := 0
	player2Wins := 0

	for _, movePair := range moves {
		winner := g.rules.GetWinner(movePair[0], movePair[1])
		switch winner {
		case 1:
			player1Wins++
		case 2:
			player2Wins++
		}
	}

	if player1Wins > player2Wins {
		return "Player 1"
	} else if player2Wins > player1Wins {
		return "Player 2"
	} else {
		return "Tie"
	}
}

func main() {
	moves := [][2]Move{
		{Rock, Scissors},
		{Scissors, Rock},
		{Paper, Scissors},
	}

	game := NewGame(NewGameRules())
	result := game.CalculateWinner(moves)
	fmt.Println("Result:", result)
}
