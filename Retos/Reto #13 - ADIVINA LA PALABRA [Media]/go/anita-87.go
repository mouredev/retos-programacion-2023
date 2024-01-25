package main

import (
	"bufio"
	"fmt"
	"log"
	"math/rand"
	"os"
	"strings"
)

var words = []string{
	"red", "yellow", "green", "blue", "purple",
	"white", "black", "pink", "orange", "grey",
}

var hiddenLetters map[string]int = make(map[string]int)

func main() {
	endGame := false
	wordInPlay := selectWord()
	printedWord, tries := hideLettersAndGetTries(wordInPlay)
	fmt.Printf("Guess the following word '%s' in %d tries. \n", printedWord, tries)

	reader := bufio.NewReader(os.Stdin)

	for tries > 0 && !endGame {
		letter, err := reader.ReadString('\n')
		if err != nil {
			log.Fatal(err)
		}
		letter = strings.ReplaceAll(letter, "\n", "")
		if len(letter) == len(wordInPlay) {
			if letter == wordInPlay {
				fmt.Printf("Word guessed correctly!! %s\n", wordInPlay)
				endGame = true
			} else {
				tries--
			}
		} else {
			index, ok := hiddenLetters[letter]
			if ok {
				printedWord = printedWord[:index] + letter + printedWord[index+1:]
				fmt.Printf("Letter %s correctly guessed! \nCurrent word is %s. Tries left: %d\n", letter, printedWord, tries)
				delete(hiddenLetters, letter)
				if !strings.Contains(printedWord, "_") {
					fmt.Println("You guessed correctly!!")
					endGame = true
				}
			}
			tries--
		}
	}
	fmt.Println("Oh! You lost the game. No more tries left")
}

func selectWord() string {
	min := 0
	max := 9
	index := rand.Intn(max-min) + min
	return words[index]
}

func hideLettersAndGetTries(w string) (string, int) {
	lettersToHide := len(w) * 60 / 100
	wordToPrint := w

	for i := 1; i <= lettersToHide; i++ {
		min := 0
		max := len(w)
		index := rand.Intn(max-min) + min
		hiddenLetters[string(w[index])] = index
		wordToPrint = wordToPrint[:index] + "_" + wordToPrint[index+1:]
	}
	return string(wordToPrint), lettersToHide
}
