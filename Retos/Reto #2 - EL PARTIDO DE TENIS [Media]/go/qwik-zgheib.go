package main

import (
	"fmt"
)

type Scoreboard struct {
	player1Points int
	player2Points int
}

type Game interface {
	PointWonBy(player string)
	CurrentScore() string
	HasWinner() bool
}

type TennisGame struct {
	scoreboard *Scoreboard
}

func NewTennisGame() *TennisGame {
	return &TennisGame{
		scoreboard: &Scoreboard{player1Points: 0, player2Points: 0},
	}
}

func (tg *TennisGame) PointWonBy(player string) {
	switch player {
	case "P1":
		tg.scoreboard.player1Points++
	case "P2":
		tg.scoreboard.player2Points++
	default:
		fmt.Println("Invalid player input. Use 'P1' or 'P2'.")
	}
}

func (tg *TennisGame) CurrentScore() string {
	if tg.HasWinner() {
		return tg.winner()
	}
	if tg.hasAdvantage() {
		return tg.advantagePlayer()
	}
	if tg.isDeuce() {
		return "Deuce"
	}
	return tg.formatScore()
}

func (tg *TennisGame) pointsToScore(points int) string {
	switch points {
	case 0:
		return "Love"
	case 1:
		return "15"
	case 2:
		return "30"
	case 3:
		return "40"
	default:
		return ""
	}
}

func (tg *TennisGame) formatScore() string {
	return fmt.Sprintf("%s - %s",
		tg.pointsToScore(tg.scoreboard.player1Points),
		tg.pointsToScore(tg.scoreboard.player2Points))
}

func (tg *TennisGame) isDeuce() bool {
	return tg.scoreboard.player1Points >= 3 && tg.scoreboard.player2Points == tg.scoreboard.player1Points
}

func (tg *TennisGame) hasAdvantage() bool {
	return (tg.scoreboard.player1Points >= 4 || tg.scoreboard.player2Points >= 4) &&
		(tg.scoreboard.player1Points-tg.scoreboard.player2Points == 1 || tg.scoreboard.player2Points-tg.scoreboard.player1Points == 1)
}

func (tg *TennisGame) advantagePlayer() string {
	if tg.scoreboard.player1Points > tg.scoreboard.player2Points {
		return "Advantage P1"
	}
	return "Advantage P2"
}

func (tg *TennisGame) HasWinner() bool {
	return (tg.scoreboard.player1Points >= 4 || tg.scoreboard.player2Points >= 4) &&
		(tg.scoreboard.player1Points-tg.scoreboard.player2Points >= 2 || tg.scoreboard.player2Points-tg.scoreboard.player1Points >= 2)
}

func (tg *TennisGame) winner() string {
	if tg.scoreboard.player1Points > tg.scoreboard.player2Points {
		return "P1 Wins"
	}
	return "P2 Wins"
}

func main() {
	game := NewTennisGame()
	points := []string{"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"}

	for _, point := range points {
		game.PointWonBy(point)
		fmt.Println(game.CurrentScore())
		if game.HasWinner() {
			break
		}
	}
}
