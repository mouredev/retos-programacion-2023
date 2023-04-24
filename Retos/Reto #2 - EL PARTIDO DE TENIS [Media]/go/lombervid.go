package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"os/exec"
	"runtime"
	"strings"
)

var scoreDescriptions = map[int]string{
	0: "Love",
	1: "15",
	2: "30",
	3: "40",
}

/******** player declaration ********/
type player struct {
	score int
}

func (p *player) Score() int {
	return p.score
}

func (p *player) IncreaseScore() {
	p.score++
}

func (p *player) ScoreDescription() string {
	return scoreDescriptions[p.Score()]
}

/******** TennisMatch declaration ********/
type TennisMatch struct {
	player1      player
	player2      player
	isFinished   bool
	scoreHistory []string
}

// Private methods
func (tm *TennisMatch) addHistory(record string) {
	tm.scoreHistory = append(tm.scoreHistory, record)
}

func (tm *TennisMatch) addScore() {
	switch true {
	case tm.IsTie() && (tm.player1.Score() >= 3):
		tm.addHistory("Deuce")
	case (tm.player1.Score() <= 3) && (tm.player2.Score() <= 3):
		tm.addHistory(fmt.Sprintf("%s - %s", tm.player1.ScoreDescription(), tm.player2.ScoreDescription()))
	case (tm.player1.Score() - tm.player2.Score()) > 1:
		tm.addHistory("Ha ganado el Player 1")
		tm.FinishGame()
	case (tm.player2.Score() - tm.player1.Score()) > 1:
		tm.addHistory("Ha ganado el Player 2")
		tm.FinishGame()
	case tm.player1.Score() > tm.player2.Score():
		tm.addHistory("Ventaja Player 1")
	case tm.player2.Score() > tm.player1.Score():
		tm.addHistory("Ventaja Player 2")
	}
}

// Public methods
func (tm *TennisMatch) IsTie() bool {
	return tm.player1.Score() == tm.player2.Score()
}

func (tm *TennisMatch) FinishGame() {
	tm.isFinished = true
}

func (tm *TennisMatch) HasFinished() bool {
	return tm.isFinished
}

func (tm *TennisMatch) Result() {
	if len(tm.scoreHistory) == 0 {
		return
	}

	center := func(s string, w int) string {
		return fmt.Sprintf("%[1]*s", -w, fmt.Sprintf("%[1]*s", (w+len(s))/2, s))
	}

	fmt.Println(strings.Repeat("—", 30))
	fmt.Println(center("Match Result", 30))
	fmt.Println(strings.Repeat("—", 30))
	fmt.Println("")

	for _, score := range tm.scoreHistory {
		width := 28
		if strings.Contains(score, "Love") {
			width = 30
		}
		fmt.Println(center(score, width))
	}

	fmt.Println("")
	fmt.Println(strings.Repeat("—", 30))
	fmt.Println("")
}

func (tm *TennisMatch) Start() {
	reader := bufio.NewReader(os.Stdin)

	for !tm.HasFinished() {
		clear()
		tm.Result()

		input := getInput(reader, "Insert winning player (P1/P2): ")
		switch strings.ToUpper(input) {
		case "P1":
			tm.player1.IncreaseScore()
			tm.addScore()
		case "P2":
			tm.player2.IncreaseScore()
			tm.addScore()
		default:
			fmt.Printf("\nInvalid option %q, please select between P1/P2. ", input)
			getInput(reader, "Press 'Enter' key to continue...")
		}
	}

	clear()
	tm.Result()
}

/******** TennisMatch constructor ********/
func NewTennisMatch() *TennisMatch {
	return &TennisMatch{}
}

/******** Normal functions ********/
func getInput(r *bufio.Reader, msg string) string {
	fmt.Print(msg)

	input, err := r.ReadString('\n')
	if err != nil {
		log.Fatal("An error has ocurred reading the input.")
	}

	return strings.TrimSpace(input)
}

func runCommand(name string, args ...string) {
	cmd := exec.Command(name, args...)
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func clear() {
	switch runtime.GOOS {
	case "windows":
		runCommand("cmd", "/c", "cls")
	case "linux", "darwin":
		runCommand("clear")
	}
}

func main() {
	NewTennisMatch().Start()
}
