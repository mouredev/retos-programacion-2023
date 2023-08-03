package main

import (
	"fmt"
	"strconv"
)

// funcion para comprobar si es un numero
func IsNumber(n string) bool {
	_, err := strconv.Atoi(n)
	if err != nil {
		return false
	}
	return true
}

// funcion para validar si tiene algun operador
func IsOperator(n string) bool {
	validOperators := []string{"+", "-", "*", "/", "%"}
	for _, exp := range validOperators {
		if n == exp {
			return true
		}
	}
	return false
}

// funcion para validar la expresion
func ValidExpression(express string, isexpr *bool) {
	for _, cr := range express {
		if IsNumber(string(cr)) || IsOperator(string(cr)) || string(cr) == " " {
			*isexpr = true
		} else {
			*isexpr = false
			break
		}
	}
}

func main() {
	express := "5 + 6 / 7 * 8"
	var isexpr bool

	ValidExpression(express, &isexpr)

	if isexpr {
		fmt.Printf("the expression %v is a math expression \n", express)
	} else {
		fmt.Printf("the expression %v is not math expression \n", express)
	}
}
