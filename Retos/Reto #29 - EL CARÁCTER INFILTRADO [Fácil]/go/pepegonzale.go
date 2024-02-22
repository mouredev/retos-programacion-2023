package main

import (
	"fmt"
)

func main() {
	caracter_infiltrado("Me llamo mouredev", "Me llemo mouredov")
	caracter_infiltrado("Me llamo.Brais Moure", "Me llamo brais moure")
}

func caracter_infiltrado(word1 string, word2 string) []string {
	var characters_infiltrados int = 0
	var array = [2]string{word1, word2}
	var characters []string
	for i := 0; i < len(array)-1; i++ {
		for j := 0; j < len(array[i])-1; j++ {
			if array[i][j] != array[i+1][j] {
				characters_infiltrados++

				characters = append(characters, string(array[i+1][j]))
			}
		}

	}
	fmt.Println(word1, " / ", word2, " => ", characters)
	return characters
}
