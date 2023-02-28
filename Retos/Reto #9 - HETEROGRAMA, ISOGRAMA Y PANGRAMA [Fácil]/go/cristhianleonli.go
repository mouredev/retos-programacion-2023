package main

import (
	"fmt"
)

const alphabet = "abcdefghijklmnopqrstuvwxyz"

func isLetter(char rune) bool {
	for _, letter := range alphabet {
		if char == letter {
			return true
		}
	}

	return false
}

// word or phrase in which no letter of the alphabet occurs more than once.
func isHeterogram(text string) bool {
	count := make(map[rune]int)

	for _, char := range text {
		if !isLetter(char) {
			continue
		}

		if _, contains := count[char]; contains {
			return false
		}

		count[char] = 1
	}

	return true
}

// word or phrase in which each letter occurs the same number of times.
func isIsogram(text string) bool {
	count := make(map[rune]int)

	for _, char := range text {
		if !isLetter(char) {
			continue
		}

		if _, contains := count[char]; !contains {
			count[char] = 0
		}

		count[char] += 1
	}

	var occurrence = 0

	for _, value := range count {
		if occurrence == 0 {
			occurrence = value
		}

		if value != occurrence {
			return false
		}
	}

	return true
}

// A pangram or holoalphabetic sentence is a sentence using every letter of a given alphabet at least once.
func isPangram(sentence string) bool {
	count := make(map[rune]int)

	for _, letter := range alphabet {
		count[letter] = 0
	}

	for _, letter := range sentence {
		if !isLetter(letter) {
			continue
		}

		count[letter] += 1
	}

	for _, occurence := range count {
		if occurence < 1 {
			return false
		}
	}

	return true
}

func main() {
	testCases := []string{
		"waltz, nymph, for quick jigs vex bud", // pg
		"bright vixens jump; dozy fowl quack",  // pg
		"authorized",                           // hg, ig
		"purchasing",                           // hg, ig
		"dodo",                                 // ig
	}

	for _, word := range testCases {
		fmt.Println(word)

		if isHeterogram(word) {
			fmt.Println("* heterogram")
		}

		if isIsogram(word) {
			fmt.Println("* isogram")
		}

		if isPangram(word) {
			fmt.Println("* pangram")
		}

		fmt.Println("=============")
	}
}
