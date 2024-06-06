package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

type WordSelector interface {
	GetRandomWord() string
}

type WordGame interface {
	Start()
}

type SimpleWordSelector struct {
	words []string
}

func NewSimpleWordSelector(words []string) *SimpleWordSelector {
	return &SimpleWordSelector{words: words}
}

func (s *SimpleWordSelector) GetRandomWord() string {
	src := rand.NewSource(time.Now().UnixNano())
	random := rand.New(src)
	return s.words[random.Intn(len(s.words))]
}

type SimpleWordGame struct {
	selector WordSelector
	attempts int
}

func NewSimpleWordGame(selector WordSelector, attempts int) *SimpleWordGame {
	return &SimpleWordGame{selector: selector, attempts: attempts}
}

func (swg *SimpleWordGame) Start() {
	word := swg.selector.GetRandomWord()
	maskedWord := maskWord(word)
	fmt.Printf("Guess the word: %s\n", maskedWord)
	fmt.Printf("You have %d attempts\n", swg.attempts)

	for swg.attempts > 0 {
		var guess string
		fmt.Print("Enter a letter or the full word: ")
		fmt.Scanln(&guess)
		guess = strings.TrimSpace(guess)

		if len(guess) == 1 {
			if strings.Contains(word, guess) {
				maskedWord = revealLetters(word, maskedWord, guess)
				fmt.Printf("Correct! %s\n", maskedWord)
			} else {
				swg.attempts--
				fmt.Printf("Incorrect. Attempts left: %d\n", swg.attempts)
			}
		} else if guess == word {
			fmt.Println("Congratulations! You guessed the word!")
			return
		} else {
			swg.attempts--
			fmt.Printf("Incorrect. Attempts left: %d\n", swg.attempts)
		}

		if maskedWord == word {
			fmt.Println("Congratulations! You guessed all the letters!")
			return
		}
	}

	fmt.Printf("You lost! The word was: %s\n", word)
}

func maskWord(word string) string {
	src := rand.NewSource(time.Now().UnixNano())
	rand.New(src)
	lettersToHide := len(word) * 60 / 100
	letters := []rune(word)
	for lettersToHide > 0 {
		index := rand.Intn(len(letters))
		if letters[index] != '_' {
			letters[index] = '_'
			lettersToHide--
		}
	}
	return string(letters)
}

func revealLetters(word, maskedWord, guess string) string {
	result := []rune(maskedWord)
	for i, c := range word {
		if string(c) == guess {
			result[i] = c
		}
	}
	return string(result)
}

func main() {
	words := []string{
		"abracadabra", "banana", "dinosaur", "elephant", "giraffe",
		"hippopotamus", "kangaroo", "pineapple", "rhinoceros", "umbrella",
	}
	selector := NewSimpleWordSelector(words)
	game := NewSimpleWordGame(selector, 5)
	game.Start()
}
