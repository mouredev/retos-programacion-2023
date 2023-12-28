package main

func main() {
	g1 := [][]string{{"🗿", "📄"}, {"🗿", "✄"}, {"🗿", "🦎"}} // Player 1
	g2 := [][]string{{"🖖", "📄"}, {"🦎", "📄"}, {"🖖", "🖖"}} // Tie
	g3 := [][]string{{"🦎", "🦎"}, {"📄", "🖖"}, {"🗿", "🦎"}} // Player 1
	g4 := [][]string{{"🗿", "📄"}, {"🗿", "✄"}, {"🦎", "🦎"}} // Tie
	g5 := [][]string{{"✄", "🖖"}, {"🦎", "✄"}, {"📄", "✄"}} // Player 2

	play(g1)
	play(g2)
	play(g3)
	play(g4)
	play(g5)
}

func play(games [][]string) {
	stateMachine := map[string]map[string]int8{
		"stone": {
			"stone":  0,
			"paper":  -1,
			"scisor": 1,
			"lizard": 1,
			"spock":  -1,
		},
		"paper": {
			"stone":  1,
			"paper":  0,
			"scisor": -1,
			"lizard": -1,
			"spock":  1,
		},
		"scisor": {
			"stone":  -1,
			"paper":  1,
			"scisor": 0,
			"lizard": 1,
			"spock":  -1,
		},
		"lizard": {
			"stone":  -1,
			"paper":  1,
			"scisor": -1,
			"lizard": 0,
			"spock":  1,
		},
		"spock": {
			"stone":  1,
			"paper":  -1,
			"scisor": 1,
			"lizard": -1,
			"spock":  0,
		},
	}

	emojiToString := map[string]string{
		"🗿": "stone",
		"📄": "paper",
		"✄": "scisor",
		"🦎": "lizard",
		"🖖": "spock",
	}

	var sum int8
	for _, game := range games {
		player1 := emojiToString[game[0]]
		player2 := emojiToString[game[1]]
		sum += stateMachine[player1][player2]
	}
	switch {
	case sum == 0:
		println("Tie")
	case sum > 0:
		println("Player 1 wins")
	case sum < 0:
		println("Player 2 wins")
	}
}
