package main

import (
	"fmt"
	"math/rand"
	"strings"
)

type Word struct {
	CurrentState string
	targetState  string
	MaxGuesses   int
	Guessed      bool
}

func main() {
	newWord := NewWord()
	newWord.Play()
}

func (w *Word) Play() {
	for !w.Guessed && w.MaxGuesses > 0 {
		println(w.CurrentState)
		println("Guesses left:", w.MaxGuesses)
		println("Enter your guess:")
		var guess string
		_, _ = fmt.Scanln(&guess)
		w.Guess(guess)
	}

	println(w.targetState)
	if w.Guessed {
		println("You won!")
	} else {
		println("You lost!")
	}
}

func (w *Word) Guess(guess string) {
	if guess == w.targetState {
		w.CurrentState = w.targetState
		w.Guessed = true
		return
	}

	if len(guess) > 1 {
		w.MaxGuesses--
		return
	}

	if strings.Contains(w.targetState, guess) && !strings.Contains(w.CurrentState, guess) {
		for i, char := range w.targetState {
			if string(char) == guess {
				w.CurrentState = w.CurrentState[:i] + guess + w.CurrentState[i+1:]
			}
		}
		if w.CurrentState == w.targetState {
			w.Guessed = true
		}
		return
	}

	w.MaxGuesses--
}

func NewWord() *Word {
	wordsPool := []string{
		"cigarette",
		"fabricate",
		"absorption",
		"champagne",
		"sentiment",
		"negotiation",
		"eavesdrop",
		"reservoir",
	}

	rand.Shuffle(len(wordsPool), func(i, j int) {
		wordsPool[i], wordsPool[j] = wordsPool[j], wordsPool[i]
	})

	currentState, targetState := wordsPool[0], wordsPool[0]
	lettersToRemove := len(currentState) - int(float64(len(currentState))*0.6)

	shuffled := strings.Split(currentState, "")
	rand.Shuffle(len(shuffled), func(i, j int) {
		shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
	})

	for _, char := range shuffled {
		currentState = strings.ReplaceAll(currentState, string(char), "_")
		count := strings.Count(currentState, "_")
		if count >= lettersToRemove {
			break
		}
	}

	return &Word{
		CurrentState: currentState,
		targetState:  targetState,
		MaxGuesses:   3,
	}
}
