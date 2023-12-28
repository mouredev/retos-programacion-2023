package main

import (
	"errors"
	"fmt"
)

type Option string

const (
	Rock     Option = "🗿"
	Paper    Option = "📄"
	Scissors Option = "✂️"
	Lizard   Option = "🦎"
	Spock    Option = "🖖"
)

type Strongness [2]Option
type Options map[Option]Strongness

var options = Options{
	Rock:     {Lizard, Scissors},
	Paper:    {Rock, Spock},
	Scissors: {Paper, Lizard},
	Lizard:   {Spock, Paper},
	Spock:    {Scissors, Rock},
}

func (wn Strongness) Contains(symbol Option) bool {
	for _, opt := range wn {
		if opt == symbol {
			return true
		}
	}
	return false
}

type GameOption struct {
	symbol Option
	winsTo Strongness
}

func (gopt GameOption) Wins(option GameOption) bool {
	return gopt.winsTo.Contains(option.symbol)
}

func NewGameOption(symbol Option) (*GameOption, error) {
	if winsTo, ok := options[symbol]; ok {
		return &GameOption{symbol, winsTo}, nil
	}
	return nil, errors.New("Invalid Option")
}

type GameMatch struct {
	p1 *GameOption
	p2 *GameOption
}

type LizardSpockGame struct {
	score1  int
	score2  int
	options []GameMatch
}

func (lsg *LizardSpockGame) resetScores() {
	lsg.score1 = 0
	lsg.score2 = 0
}

func (lsg *LizardSpockGame) SetInputs(inputs [][2]Option) *LizardSpockGame {
	var options []GameMatch

	for i, match := range inputs {
		opt1, err := NewGameOption(match[0])
		if err != nil {
			panic(fmt.Sprintf("%s (at index %d:0)", err, i))
		}

		opt2, err := NewGameOption(match[1])
		if err != nil {
			panic(fmt.Sprintf("%s (at index %d:1)", err, i))
		}

		options = append(options, GameMatch{opt1, opt2})
	}

	lsg.options = options

	return lsg
}

func (lsg *LizardSpockGame) Play() string {
	lsg.resetScores()

	for _, option := range lsg.options {
		if option.p1.Wins(*option.p2) {
			lsg.score1++
		}
		if option.p2.Wins(*option.p1) {
			lsg.score2++
		}
	}

	if lsg.score1 > lsg.score2 {
		return "Player 1"
	}

	if lsg.score2 > lsg.score1 {
		return "Player 2"
	}

	return "Tie"
}

func main() {
	var failures int
	tests := []struct {
		input [][2]Option
		want  string
	}{
		{
			[][2]Option{{"🗿", "✂️"}, {"✂️", "🗿"}, {"📄", "✂️"}},
			"Player 2",
		},
		{
			[][2]Option{{"🖖", "✂️"}, {"📄", "🗿"}, {"✂️", "🦎"}, {"🖖", "🦎"}, {"📄", "🗿"}},
			"Player 1",
		},
		{
			[][2]Option{{"🖖", "🖖"}},
			"Tie",
		},
		{
			[][2]Option{{"🖖", "🗿"}, {"🦎", "✂️"}, {"📄", "🖖"}, {"🦎", "🗿"}},
			"Tie",
		},
	}

	game := &LizardSpockGame{}

	for i, test := range tests {
		func() {
			defer func() {
				if r := recover(); r != nil {
					failures++
					fmt.Printf("Test %d failed with message: %q\n", i, r)
				}
			}()

			got := game.SetInputs(test.input).Play()

			if got != test.want {
				failures++
				fmt.Printf("Test %d failed: got %q, want %q\n", i, got, test.want)
				return
			}

			fmt.Println(got)
		}()
	}

	if failures == 0 {
		fmt.Println("All tests passed")
	}
}
