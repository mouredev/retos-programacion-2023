/*
 * Pues me he venido un poco arriba...
 * No es la mejor implementación, pero me ha hecho gracia dejarla así...
 * Salen palabras un poco raras consultando la página...
 * No me lo tengáis muy en cuenta... :P
 */

package main

import (
	"fmt"
	"io/ioutil"
	"math/rand"
	"net/http"
	"os"
	"strings"
	"time"
)

func selectWord() (string, string) {
	rand.Seed(time.Now().UnixNano())

	// Find a word (in spanish) by consulting a public API
	resp, err := http.Get("https://random-word-api.herokuapp.com/word?lang=es")
	if err != nil {
		fmt.Println("No response from request")
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)

	//Response returned in this format ["word"].
	// Remove special char in the formatWord func to format the string
	selectedWord := formatWord(body)

	// Split the string into its chars
	letters := strings.Split(selectedWord, "")
	// Creates a map to add char by char the hidden word
	hidden := make([]string, len(letters))
	// Maximum of chars we're going to hide
	maxHidden := int(float64(len(letters)) * 0.6)

	//We move through the word letter by letter and then randomly decide whether to hide that letter
	hiddenCount := 0
	for i := 0; i < len(letters); i++ {
		//if rand.Float64() < 0.5 && hiddenCount < maxHidden {
		if rand.Intn(2) == 0 && hiddenCount < maxHidden {
			hidden[i] = "_"
			hiddenCount++
		} else {
			hidden[i] = letters[i]
		}
	}
	return strings.Join(hidden, ""), selectedWord
}

func formatWord(input []byte) string {
	//Replace special character we found in the API call
	word := strings.ToLower(strings.NewReplacer("á", "a", "é", "e", "í", "i", "ó", "o", "ú", "u", "\"", "", "]", "", "[", "").Replace(string(input)))
	return word
}

func main() {
	chances := 5
	hiddenWord, clearWord := selectWord()

	fmt.Println("Guess the word!!")
	fmt.Println("This is the word you have to guess: \n", hiddenWord)
	for {
		var input string
		fmt.Print("\nEnter a letter or a word (", chances, " attempts remaining): ")
		fmt.Scanln(&input)
		// If we enter a word, let's see if it's correct...
		if len(input) > 1 {
			if input == clearWord {
				fmt.Println("Wow! You guessed the word! Congrats")
				break
			} else {
				fmt.Println("This is not the word you are looking for...")
				chances--
				fmt.Println("You have", chances, "chances more. Be careful!")
				continue
			}
		}
		//We move through the word letter by letter and if the letter exists, we look at its position
		// If that position in the hidden word is a "_", we replace it with the letter.
		if strings.Contains(clearWord, input) {
			for i := 0; i < len(clearWord); i++ {
				if input == string(clearWord[i]) && string(hiddenWord[i]) == "_" {
					prefix := hiddenWord[:i]
					suffix := hiddenWord[i+1:]
					hiddenWord = strings.Join([]string{prefix, input, suffix}, "")
					if hiddenWord == clearWord {
						fmt.Println("Yeah! You guessed the word! Well done!")
						fmt.Println(hiddenWord)
						os.Exit(0)
					}
					continue
				}
			}
			fmt.Println(hiddenWord)
		} else {
			chances--
			fmt.Println("Ups! Incorrect...")
			fmt.Println(hiddenWord)
		}
		if chances == 0 {
			fmt.Println("You haven't more chances... You lose")
			fmt.Println("The word is", clearWord)
			os.Exit(0)
		}
	}
}
