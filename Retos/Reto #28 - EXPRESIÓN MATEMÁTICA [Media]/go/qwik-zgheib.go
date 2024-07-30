package main

import (
	"fmt"
	"regexp"
)

/*
type MathExpressionValidator interface {
	Validate(expression string) bool
}
*/

type SimpleMathExpressionValidator struct{}

func NewSimpleMathExpressionValidator() *SimpleMathExpressionValidator {
	return &SimpleMathExpressionValidator{}
}

func (v *SimpleMathExpressionValidator) Validate(expression string) bool {
	regex := regexp.MustCompile(`^-?\d+(\.\d+)?([ \t]+[+\-*/%][ \t]+-?\d+(\.\d+)?)*$`)
	return regex.MatchString(expression)
}

func ValidateMathExpression(expression string) bool {
	validator := NewSimpleMathExpressionValidator()
	return validator.Validate(expression)
}

func main() {
	expressions := []string{
		"5 + 6 / 7 - 4",
		"5 a 6",
		"-3.5 * 2 + 4.2 / -1.1",
		"10 +",
		"5 5 + 6",
	}

	for _, expr := range expressions {
		valid := ValidateMathExpression(expr)
		fmt.Printf("Expression: \"%s\" is valid --> %t\n", expr, valid)
	}
}


/* 
	* if use to test: create file <name>_test.go, with this content and execute with go test -v
	* install package <github.com/stretchr/testify/assert> with go get -u github.com/stretchr/testify/assert


package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestValidateMathExpression(t *testing.T) {
	tests := []struct {
		expression string
		expected   bool
	}{
		{"5 + 6 / 7 - 4", true},
		{"5 a 6", false},
		{"-3.5 * 2 + 4.2 / -1.1", true},
		{"10 +", false},
		{"5 5 + 6", false},
		{"10 / 2 - 3 * 4", true},
		{"-10 + -20 - -30", true},
		{"1 + 1.1.1", false},
	}

	for _, test := range tests {
		result := ValidateMathExpression(test.expression)
		assert.Equal(t, test.expected, result)
	}
}
*/