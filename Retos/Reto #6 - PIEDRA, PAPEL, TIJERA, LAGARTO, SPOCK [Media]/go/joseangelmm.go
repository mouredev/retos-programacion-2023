package main

import "fmt"

type round struct {
	player1game, player2game interface{}
}

func main() {
	play([]round{{"🗿", "📄"}, {"🗿", "✄"}, {"🗿", "🦎"}}) // Player 1
	play([]round{{"🖖", "📄"}, {"🦎", "📄"}, {"🖖", "🦎"}}) // Tie
	play([]round{{"🦎", "🦎"}, {"📄", "🖖"}, {"🗿", "🦎"}}) // Player 1
	play([]round{{"🗿", "📄"}, {"🗿", "✄"}, {"🖖", "🦎"}}) // Tie
	play([]round{{"✄", "🖖"}, {"🦎", "✄"}, {"📄", "✄"}}) // Player 2
}

func play(rounds []round) {

	var roundsWonByPlayer1 int8

	for _, round := range rounds {
		switch round.player1game {
		case "🗿":
			roundsWonByPlayer1 += rock(round.player2game)
		case "📄":
			roundsWonByPlayer1 += paper(round.player2game)
		case "✄":
			roundsWonByPlayer1 += scissors(round.player2game)
		case "🦎":
			roundsWonByPlayer1 += spock(round.player2game)
		case "🖖":
			roundsWonByPlayer1 += lizard(round.player2game)
		}
	}

	if roundsWonByPlayer1 > int8(0) {
		fmt.Println("Player 1")
	} else if roundsWonByPlayer1 < int8(0) {
		fmt.Println("Player 2")
	} else {
		fmt.Println("Tie")
	}

}

func rock(rivalGame interface{}) int8 {
	switch rivalGame {
	case "📄":
		return -1
	case "✄":
		return 1
	case "🦎":
		return 1
	case "🖖":
		return -1
	}
	return 0
}

func paper(rivalGame interface{}) int8 {
	switch rivalGame {
	case "🗿":
		return 1
	case "✄":
		return -1
	case "🦎":
		return -1
	case "🖖":
		return 1
	}
	return 0
}

func scissors(rivalGame interface{}) int8 {
	switch rivalGame {
	case "🗿":
		return -1
	case "📄":
		return 1
	case "🦎":
		return 1
	case "🖖":
		return -1
	}
	return 0
}

func spock(rivalGame interface{}) int8 {
	switch rivalGame {
	case "🗿":
		return 1
	case "📄":
		return -1
	case "🦎":
		return -1
	case "✄":
		return 1
	}
	return 0
}

func lizard(rivalGame interface{}) int8 {
	switch rivalGame {
	case "🗿":
		return -1
	case "📄":
		return 1
	case "🖖":
		return 1
	case "✄":
		return -1
	}
	return 0
}
