package main

import (
	"fmt"
	"strings"
)

const ALPHABET = "abcdefghijklmnopqrstuvwxyz"

// comprobar  isHeterogram
func IsHeterogram(text string) bool {
	var het bool = true

	for _, let := range strings.ToUpper(ALPHABET) {
		count := strings.Count(strings.ToUpper(text), string(let))
		if count > 1 {
			het = false
			break
		}
	}
	return het

}

func IsIsogram(text string) bool {
	var occurrence int = 0
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

// funcion para saber si el texto es un pangrama
func IsPangram(text string) bool {
	var pan bool = true
	for _, let := range strings.ToUpper(ALPHABET) {
		con := strings.Contains(strings.ToUpper(text), string(let))
		if con == false {
			pan = false
		}
	}
	return pan
}

// funcion para comprobar letras
func isLetter(char rune) bool {
	for _, letter := range strings.ToUpper(ALPHABET) {
		if char == letter {
			return true
		}
	}

	return false
}

func main() {
	text1 := "centrifugado"
	text2 := "escritura"
	text3 := "Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú"

	fmt.Println(IsHeterogram(text1))
	fmt.Println(IsPangram(text3))
	fmt.Println(IsIsogram(text2))
}
