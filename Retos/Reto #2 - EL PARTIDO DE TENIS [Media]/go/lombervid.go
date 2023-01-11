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

func printResult(scores []string) {
	if len(scores) == 0 {
		return
	}

	center := func(s string, w int) string {
		return fmt.Sprintf("%[1]*s", -w, fmt.Sprintf("%[1]*s", (w+len(s))/2, s))
	}

	fmt.Println(strings.Repeat("—", 30))
	fmt.Println(center("Match Result", 30))
	fmt.Println(strings.Repeat("—", 30))
	fmt.Println("")

	for _, score := range scores {
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

func getScore(p1 int, p2 int) (score string, finished bool) {
	scoreTerms := map[int]string{0: "Love", 1: "15", 2: "30", 3: "40"}
	p1Score := scoreTerms[p1]
	p2Score := scoreTerms[p2]

	switch true {
	case (p1 == p2) && (p1 >= 3):
		score = "Deuce"
	case (p1 <= 3) && (p2 <= 3):
		score = fmt.Sprintf("%s - %s", p1Score, p2Score)
	case (p1 - p2) > 1:
		score = "Ha ganado P1"
		finished = true
	case (p2 - p1) > 1:
		score = "Ha ganado P2"
		finished = true
	case p1 > p2:
		score = "Ventaja P1"
	case p2 > p1:
		score = "Ventaja P2"
	}

	return score, finished
}

func collectScores() []string {
	var p1, p2 int
	var finished bool
	scores := make([]string, 0)
	reader := bufio.NewReader(os.Stdin)

	for !finished {
		var score string
		printResult(scores)
		input := getInput(reader, "Insert winning player (P1/P2): ")

		switch strings.ToUpper(input) {
		case "P1":
			p1++
			score, finished = getScore(p1, p2)
			scores = append(scores, score)
		case "P2":
			p2++
			score, finished = getScore(p1, p2)
			scores = append(scores, score)
		default:
			fmt.Printf("\nInvalid option %q, please select between P1/P2. ", input)
			getInput(reader, "Press 'Enter' key to continue...")
		}
		clear()
	}

	return scores
}

func main() {
	scores := collectScores()
	printResult(scores)
}
