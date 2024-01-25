package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	fmt.Println("Write below the text you want to analyze.")
	reader := bufio.NewReader(os.Stdin)
	text, err := reader.ReadString('\n')
	failOnErr(err)

	text = strings.Trim(text, "\n")

	fmt.Printf("\n*** Statistics ***\n")
	fmt.Printf("Number of Words: %d\n", getNumberOfWords(text))
	fmt.Printf("Average Word Length: %d\n", getAverageWordLength(text))
	fmt.Printf("Number of Sentences: %d\n", getNumberOfSencentes(text))
	fmt.Printf("Longest Word: %s\n", getLongestWord(text))
}

func getNumberOfWords(text string) int {
	return len(strings.Fields(text))
}

func getAverageWordLength(text string) int {
	words := strings.Fields(text)
	accumulatedLength := 0

	for _, word := range words {
		accumulatedLength += len(word)
	}

	return accumulatedLength / len(words)
}

func getNumberOfSencentes(text string) int {
	return strings.Count(text, ".")
}

func getLongestWord(text string) string {
	words := strings.Fields(text)
	longestWord := ""
	for _, word := range words {
		if len(word) > len(longestWord) {
			longestWord = word
		}
	}
	return longestWord
}

func failOnErr(err error) {
	if err != nil {
		log.Fatalf("Error: %v", err)
	}
}
