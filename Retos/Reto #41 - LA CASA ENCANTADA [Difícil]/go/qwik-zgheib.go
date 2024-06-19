package main

import (
	"fmt"
	"math/rand"
	"strings"
)

const size = 4

type Room struct {
	hasCandy bool
	hasGhost bool
	enigma   string
	answer   string
}

var mansion [size][size]Room

var enigmas = []struct {
	question string
	answer   string
}{
	{"what is the capital of France?", "paris"},
	{"how many legs does a spider have?", "8"},
	{"in what year did man land on the moon?", "1969"},
	{"what is the longest river in the world?", "nilo"},
	{"what planet is known as the red planet?", "marte"},
}

var directions = map[string][2]int{
	"north": {0, -1},
	"south": {0, 1},
	"east":  {1, 0},
	"west":  {-1, 0},
}

func init() {
	rand.Int()

	for i := range mansion {
		for j := range mansion[i] {
			mansion[i][j] = Room{}
		}
	}

	mansion[0][0].enigma = "there is no enigma here. Forward!"

	mansion[3][2].hasCandy = true

	for i := range mansion {
		for j := range mansion[i] {
			if i == 0 && j == 0 || i == 3 && j == 2 {
				continue
			}
			enigma := enigmas[rand.Intn(len(enigmas))]
			mansion[i][j].enigma = enigma.question
			mansion[i][j].answer = enigma.answer
			mansion[i][j].hasGhost = rand.Float64() < 0.1
		}
	}
}

func askQuestion(question, answer string) bool {
	fmt.Println("question:", question)
	var response string
	_, err := fmt.Scanln(&response)
	if err != nil {
		return false
	}
	return strings.ToLower(response) == answer
}

func main() {
	x, y := 0, 0

	fmt.Println("🏰 welcome to the abandoned mansion! Your mission is to find the candy room.🍭")

	for {
		currentRoom := &mansion[y][x]
		if currentRoom.hasCandy {
			fmt.Println("you've found the candy room! 🎉🍭 congratulations!")
			break
		}

		fmt.Println("\nYou find yourself in a new room.")
		if currentRoom.hasGhost {
			fmt.Println("👻 A ghost has appeared! You must answer two questions to advance.")
			for i := 0; i < 2; i++ {
				enigma := enigmas[rand.Intn(len(enigmas))]
				if !askQuestion(enigma.question, enigma.answer) {
					fmt.Println("Wrong answer. The ghost holds you. Try again.")
					continue
				}
			}
		}

		if !askQuestion(currentRoom.enigma, currentRoom.answer) {
			fmt.Println("Wrong answer. You cannot move forward until you answer correctly.")
			continue
		}

		fmt.Println("Correct answer. Where would you like to go?")
		for dir := range directions {
			nx, ny := x+directions[dir][0], y+directions[dir][1]
			if nx >= 0 && nx < size && ny >= 0 && ny < size {
				fmt.Println("-", dir)
			}
		}

		var direction string
		_, err := fmt.Scanln(&direction)
		if err != nil {
			return
		}
		dir, valid := directions[direction]
		if !valid || x+dir[0] < 0 || x+dir[0] >= size || y+dir[1] < 0 || y+dir[1] >= size {
			fmt.Println("Invalid address. Try again.")
			continue
		}

		x += dir[0]
		y += dir[1]
	}
}
