package main

import (
	"fmt"
	"strings"
)

/* metodos de trabajo y variables estaticas*/

var ALPHA = map[string]int{
	"A": 1,
	"B": 2,
	"C": 3,
	"D": 4,
	"E": 5,
	"F": 6,
	"G": 7,
	"H": 8,
	"I": 9,
	"J": 10,
	"K": 11,
	"L": 12,
	"M": 13,
	"N": 14,
	"Ñ": 15,
	"O": 16,
	"P": 17,
	"Q": 18,
	"R": 19,
	"S": 20,
	"T": 21,
	"U": 22,
	"V": 23,
	"W": 24,
	"X": 25,
	"Y": 26,
	"Z": 27,
}

type Hundred interface {
	ReadWord()
}

/* implementar funciones */

type WordHundred struct {
	Word string
}

func (w *WordHundred) ReadWord() {

	for {
		fmt.Println("Write a word if it is worth 100 points you will win the game : ")
		fmt.Scanf("%s", &w.Word)
		if val := Validate(w.Word); val == true {
			if points := EvaluteWord(w.Word); points == 100 {
				fmt.Printf("Congratulations you have won with the world %v \n ", w.Word)
				break
			} else {
				fmt.Printf("With the word %v you have obtained %v points \n", w.Word, points)
			}
		} else {
			fmt.Println("The word must have a minimum length of 4 characters")
		}
	}

}

// funcion auxilar para evaluar la frase
func EvaluteWord(word string) (points int) {
	for _, w := range word {
		value := ALPHA[strings.ToUpper(string(w))]
		points += value
	}
	return points
}

// funcion para validar palabra
func Validate(word string) (validate bool) {
	if len(word) > 4 {
		validate = true
	}
	return validate
}

func main() {
	var hundred Hundred = &WordHundred{}
	hundred.ReadWord()
}
