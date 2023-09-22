package main

import (
	"fmt"
	"strings"
)

// definimos metodos de trabajo
type Cell interface {
	ReadData()
	GetValueColum()
}

// implementacion de los metodos de trabajo
type Excel struct {
	Colum string
}

// leer entrada del usuario
func (e *Excel) ReadData() {
	for len(e.Colum) > 3 || len(e.Colum) == 0 {
		fmt.Println("Introduce valor of the cell to search for")
		fmt.Scanf("%s", &e.Colum)
		e.Colum = strings.ToUpper(e.Colum)
		if len(e.Colum) > 3 {
			fmt.Println("the cell can only have a maximum of three characters")
		}
	}
}

// obtener valor de la celda
func (e *Excel) GetValueColum() {
	var finalValue int
	switch {
	case len(e.Colum) == 1:
		finalValue = ValueOneLetter(e.Colum)
	case len(e.Colum) == 2:
		finalValue = ValueTwoLetters(e.Colum)
	case len(e.Colum) == 3:
		finalValue = ValueThreeLetters(e.Colum)
	}
	fmt.Printf("the value of column %v is %v ", e.Colum, finalValue)
}

// valores y funciones auxiliares
const A = 1
const Z = 26

var alphabet []string = []string{"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}

// funcion para obtener el valor de tres letras
func ValueThreeLetters(letters string) int {
	value := Z*ValueTwoLetters(string(letters[:2])) + ValueOneLetter(string(letters[2]))
	return value
}

// funcion para obtener el valor de dos letras
func ValueTwoLetters(letters string) int {
	value := Z*ValueOneLetter(string(letters[0])) + ValueOneLetter(string(letters[1]))
	return value
}

// funcion para obtener el valor una sola letra
func ValueOneLetter(letter string) int {
	var value int
	switch letter {
	case "A":
		value = A
	case "Z":
		value = Z
	default:
		for ind, lett := range alphabet {
			if letter == lett {
				value = A + ind
			}
		}
	}
	return value
}

func main() {
	var cell Cell = &Excel{}
	cell.ReadData()
	cell.GetValueColum()
}
