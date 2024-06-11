package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

type WordScorer interface {
	Score(word string) int
}

type SpanishWordScorer struct {
	letterValues map[rune]int
}

func NewSpanishWordScorer() *SpanishWordScorer {
	letterValues := make(map[rune]int)
	for i, letter := range "abcdefghijklmnñopqrstuvwxyz" {
		letterValues[letter] = i + 1
	}
	return &SpanishWordScorer{letterValues: letterValues}
}

func (s *SpanishWordScorer) Score(word string) int {
	total := 0
	for _, letter := range word {
		if value, exists := s.letterValues[letter]; exists {
			total += value
		} else if unicode.IsLetter(letter) {
			fmt.Printf("unknown character'%c' ignored.\n", letter)
		}
	}
	return total
}

type UserInteractor interface {
	GetInput(prompt string) string
	PrintOutput(output string)
}

type ConsoleInteractor struct{}

func (ci *ConsoleInteractor) GetInput(prompt string) string {
	fmt.Print(prompt)
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	return scanner.Text()
}

func (ci *ConsoleInteractor) PrintOutput(output string) {
	fmt.Println(output)
}

type WordGame struct {
	scorer      WordScorer
	interactor  UserInteractor
	targetScore int
}

func NewWordGame(scorer WordScorer, interactor UserInteractor, targetScore int) *WordGame {
	return &WordGame{
		scorer:      scorer,
		interactor:  interactor,
		targetScore: targetScore,
	}
}

func (wg *WordGame) Play() {
	for {
		word := wg.interactor.GetInput("enter a word: ")
		word = strings.ToLower(strings.TrimSpace(word))
		score := wg.scorer.Score(word)
		wg.interactor.PrintOutput(fmt.Sprintf("the word insert has %d points.", score))
		if score >= wg.targetScore {
			wg.interactor.PrintOutput("you have reached or exceeded 100 points! The game is over.")
			break
		}
	}
}

func main() {
	scorer := NewSpanishWordScorer()
	interactor := &ConsoleInteractor{}
	game := NewWordGame(scorer, interactor, 100)
	game.Play()
}
