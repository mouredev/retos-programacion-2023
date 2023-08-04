package main

import (
	"fmt"
	"strconv"
)

func isNumber(character string) bool {
	if _, err := strconv.Atoi(character); err != nil {
		return false
	}
	return true
}

func isOperator(character string) bool {
	validOperators := []string{"-", "+", "*", "/", "%"}

	for _, op := range validOperators {
		if op == character {
			return true
		}
	}
	return false

}

func validateExpression(expression string, isExpression *bool) {
	whiteSpace := " "
	for _, c := range expression {
		character := string(c)
		if isNumber(character) || isOperator(character) || character == whiteSpace {
			*isExpression = true
			continue
		}

		*isExpression = false
		break
	}
}

func main() {
	expression1 := "5 + 6 / 7 - 4"
	expression2 := "5 a 6"

	var isExpression1, isExpression2 bool

	validateExpression(expression1, &isExpression1)
	validateExpression(expression2, &isExpression2)

	fmt.Printf("The expression1 '%s' is valid - %t\n", expression1, isExpression1)
	fmt.Printf("The expression2 '%s' is not valid - %t\n", expression2, isExpression2)

}
