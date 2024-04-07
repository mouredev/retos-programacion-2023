package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	fmt.Print("Enter a string to check: ")
	reader := bufio.NewReader(os.Stdin)
	word, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	word = strings.Trim(word, "\n")
	word = strings.ReplaceAll(word, " ", "")
	m := getMap(strings.ToLower(word))

	isHeterogram(word, m)
	isIsogram(word, m)
	isPangram(word, m)
}

func getMap(word string) map[string]int {
	m := map[string]int{}

	for _, l := range word {
		m[string(l)]++
	}

	return m
}

func isHeterogram(word string, wordMap map[string]int) {
	for _, v := range wordMap {
		if v > 1 {
			fmt.Printf("%s is NOT an heterogram\n", word)
			return
		}
	}
	fmt.Printf("%s is an heterogram\n", word)
}

func isIsogram(word string, wordMap map[string]int) {
	firstLetter := word[0]
	for _, v := range wordMap {
		if v != wordMap[string(firstLetter)] {
			fmt.Printf("%s is NOT an isogram\n", word)
			return
		}
	}
	fmt.Printf("%s is an isogram\n", word)
}

func isPangram(word string, wordMap map[string]int) {
	alphabet := "abcdefghijklmnopqrstuvwxyz"

	for _, l := range alphabet {
		if wordMap[string(l)] == 0 {
			fmt.Printf("%s is NOT a pangram\n", word)
			return
		}
	}
	fmt.Printf("%s is a pangram\n", word)
}
