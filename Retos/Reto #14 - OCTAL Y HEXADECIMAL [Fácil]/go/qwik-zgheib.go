package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type NumberConverter interface {
	ToOctal(decimal int) string
	ToHexadecimal(decimal int) string
}

type CustomNumberConverter struct{}

func NewCustomNumberConverter() *CustomNumberConverter {
	return &CustomNumberConverter{}
}

func (c *CustomNumberConverter) ToOctal(decimal int) string {
	if decimal == 0 {
		return "0"
	}

	isNegative := false
	if decimal < 0 {
		isNegative = true
		decimal = -decimal
	}

	octal := ""
	for decimal > 0 {
		remainder := decimal % 8
		octal = fmt.Sprintf("%d%s", remainder, octal)
		decimal = decimal / 8
	}

	if isNegative {
		octal = "-" + octal
	}

	return octal
}

func (c *CustomNumberConverter) ToHexadecimal(decimal int) string {
	if decimal == 0 {
		return "0"
	}

	isNegative := false
	if decimal < 0 {
		isNegative = true
		decimal = -decimal
	}

	hexChars := "0123456789ABCDEF"
	hexadecimal := ""
	for decimal > 0 {
		remainder := decimal % 16
		hexadecimal = fmt.Sprintf("%c%s", hexChars[remainder], hexadecimal)
		decimal = decimal / 16
	}

	if isNegative {
		hexadecimal = "-" + hexadecimal
	}

	return hexadecimal
}

func readInput(prompt string) string {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(prompt)
	input, _ := reader.ReadString('\n')
	return strings.TrimSpace(input)
}

func getValidNumber() int {
	for {
		input := readInput("Enter a valid decimal number: ")
		number, err := strconv.Atoi(input)
		if err == nil {
			return number
		}
		fmt.Println("Invalid input. Please enter a valid decimal number.")
	}
}

func main() {
	converter := NewCustomNumberConverter()

	decimalNumber := getValidNumber()
	fmt.Printf("Decimal: %d\n", decimalNumber)
	fmt.Printf("Octal: %s\n", converter.ToOctal(decimalNumber))
	fmt.Printf("Hexadecimal: %s\n", converter.ToHexadecimal(decimalNumber))
}
