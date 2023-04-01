package main

import (
	"bufio"
	"fmt"
	"log"
	"math/rand"
	"os"
	"strings"
	"time"
)

type GameManager struct {
	word           string
	chances        int
	missingLetters string
}

func (m GameManager) getConcealedWord() string {
	var result = ""

	for _, letter := range m.word {
		if strings.Contains(m.missingLetters, string(letter)) {
			result += "_"
		} else {
			result += string(letter)
		}
	}

	return result
}

func (m *GameManager) removeLetter(letter string) {
	m.missingLetters = strings.ReplaceAll(m.missingLetters, letter, "")
}

func (m *GameManager) decreaseChances() {
	m.chances -= 1
}

func (m GameManager) hasFinished() bool {
	return len(m.missingLetters) == 0
}

func main() {
	rand.Seed(time.Now().Unix())
	reader := bufio.NewReader(os.Stdin)
	word := getRandomWord()

	gameManager := GameManager{
		word:           word,
		chances:        3,
		missingLetters: concealLetters(word, 50),
	}

	for {
		fmt.Println(gameManager.getConcealedWord())
		input := readInput(reader, "Guess:")

		var madeMistake = false

		switch len([]rune(input)) {
		case 0:
			break
		case 1:
			if strings.Contains(word, input) {
				gameManager.removeLetter(input)
			} else {
				gameManager.decreaseChances()
				madeMistake = true
			}
		case len([]rune(word)):
			if input == word {
				for _, letter := range input {
					gameManager.removeLetter(string(letter))
				}
			} else {
				gameManager.decreaseChances()
				madeMistake = true
			}
		default:
			fmt.Println("Try guessing either the entire word or one letter at a time.")
		}

		if madeMistake {
			switch gameManager.chances {
			case 0:
				fmt.Println("You lost.")
				return
			case 1:
				fmt.Println("Incorrect letter. 1 try left.")
			default:
				fmt.Printf("Incorrect letter. %d tries left\n", gameManager.chances)
			}
		}

		if gameManager.hasFinished() {
			fmt.Printf("(%s) You won!\n", word)
			break
		}
	}
}

func concealLetters(word string, percentage float32) string {
	hideLetterCount := len(word) * int(percentage) / 100

	var letters = ""

	for {
		if len(letters) >= hideLetterCount {
			return letters
		}

		randomIndex := rand.Intn(len(word))
		letter := []rune(word)[randomIndex]

		if !strings.Contains(letters, string(letter)) {
			letters += string(letter)
		}
	}
}

func readInput(reader *bufio.Reader, message string) string {
	fmt.Println(message)

	input, err := reader.ReadString('\n')

	if err != nil {
		log.Fatal(err)
	}

	return strings.ReplaceAll(input, "\n", "")
}

func getRandomWord() string {
	words := []string{
		"abcdefghij",
		"challenge",
		"realisation",
		"conglomerate",
	}

	index := rand.Intn(len(words))
	return words[index]
}
