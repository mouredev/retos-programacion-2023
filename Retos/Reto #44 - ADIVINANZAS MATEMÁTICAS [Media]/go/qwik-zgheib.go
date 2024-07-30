package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	rand.Int()

	scanner := bufio.NewScanner(os.Stdin)
	correctAnswers := 0
	totalQuestions := 0
	maxDigits := 1
	timeLimit := 3 * time.Second

	for {
		totalQuestions++
		if totalQuestions > 1 && (totalQuestions-1)%5 == 0 {
			maxDigits++
		}

		a, b, op, correctAnswer := generateQuestion(maxDigits)
		fmt.Printf("question %d: how much is it %d %s %d?\n", totalQuestions, a, op, b)

		fmt.Print("answer: ")

		answerChan := make(chan string)
		go func() {
			scanner.Scan()
			answerChan <- scanner.Text()
		}()

		select {
		case answer := <-answerChan:
			answer = strings.TrimSpace(answer)
			userAnswer, err := strconv.Atoi(answer)
			if err != nil {
				fmt.Println("invalid answer. End of the game.")
				return
			}

			if userAnswer == correctAnswer {
				correctAnswers++
				fmt.Println("correct!")
			} else {
				fmt.Printf("incorrect. The correct answer was %d\n", correctAnswer)
			}

		case <-time.After(timeLimit):
			fmt.Println("time out. End of the game.")
			fmt.Printf("correct answers %d\n", correctAnswers)
			return
		}
	}
}

func generateQuestion(maxDigits int) (int, int, string, int) {
	ops := []string{"+", "-", "*", "/"}
	op := ops[rand.Intn(len(ops))]

	a := rand.Intn(intPow(10, maxDigits))
	b := rand.Intn(intPow(10, maxDigits))

	if op == "/" && b == 0 {
		b = 1
	}

	var correctAnswer int
	switch op {
	case "+":
		correctAnswer = a + b
	case "-":
		correctAnswer = a - b
	case "*":
		correctAnswer = a * b
	case "/":
		correctAnswer = a / b
	}

	return a, b, op, correctAnswer
}

func intPow(base, exp int) int {
	result := 1
	for exp > 0 {
		result *= base
		exp--
	}
	return result
}
