package main

import (
	"bufio"
	"crypto/rand"
	"fmt"
	"math/big"
	"os"
	"strconv"
	"strings"
)

type PasswordGenerator interface {
	Generate(length int, useUppercase, useNumbers, useSymbols bool) (string, error)
}

type RandomPasswordGenerator struct {
	lowercaseLetters string
	uppercaseLetters string
	numbers          string
	symbols          string
}

func NewRandomPasswordGenerator() *RandomPasswordGenerator {
	return &RandomPasswordGenerator{
		lowercaseLetters: "abcdefghijklmnopqrstuvwxyz",
		uppercaseLetters: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
		numbers:          "0123456789",
		symbols:          "!@#$%^&*()-_=+[]{}|;:,.<>?/",
	}
}

func (rpg *RandomPasswordGenerator) Generate(length int, useUppercase, useNumbers, useSymbols bool) (string, error) {
	if length < 8 || length > 16 {
		return "", fmt.Errorf("password length must be between 8 and 16")
	}

	charPool := rpg.lowercaseLetters
	if useUppercase {
		charPool += rpg.uppercaseLetters
	}
	if useNumbers {
		charPool += rpg.numbers
	}
	if useSymbols {
		charPool += rpg.symbols
	}

	if len(charPool) == 0 {
		return "", fmt.Errorf("character pool is empty")
	}

	var password strings.Builder
	for i := 0; i < length; i++ {
		index, err := rand.Int(rand.Reader, big.NewInt(int64(len(charPool))))
		if err != nil {
			return "", err
		}
		password.WriteByte(charPool[index.Int64()])
	}

	return password.String(), nil
}

func getInput(prompt string) string {
	fmt.Print(prompt)
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	return strings.TrimSpace(input)
}

func parseBoolInput(input string) (bool, error) {
	input = strings.ToLower(input)
	if input == "" || input == "y" {
		return true, nil
	} else if input == "n" {
		return false, nil
	} else {
		return false, fmt.Errorf("invalid input")
	}
}

func main() {
	pg := NewRandomPasswordGenerator()

	var length int
	var err error

	for {
		lengthInput := getInput("Enter password length (8-16): ")
		length, err = strconv.Atoi(lengthInput)
		if err == nil && length >= 8 && length <= 16 {
			break
		}
		fmt.Println("Invalid length. Please enter a number between 8 and 16.")
	}

	useUppercase := false
	for {
		useUppercaseInput := getInput("Include uppercase letters? [Y/n]: ")
		useUppercase, err = parseBoolInput(useUppercaseInput)
		if err == nil {
			break
		}
		fmt.Println("Invalid input for uppercase letters. Please enter Y or n.")
	}

	useNumbers := false
	for {
		useNumbersInput := getInput("Include numbers? [Y/n]: ")
		useNumbers, err = parseBoolInput(useNumbersInput)
		if err == nil {
			break
		}
		fmt.Println("Invalid input for numbers. Please enter Y or n.")
	}

	useSymbols := false
	for {
		useSymbolsInput := getInput("Include symbols? [Y/n]: ")
		useSymbols, err = parseBoolInput(useSymbolsInput)
		if err == nil {
			break
		}
		fmt.Println("Invalid input for symbols. Please enter Y or n.")
	}

	password, err := pg.Generate(length, useUppercase, useNumbers, useSymbols)
	if err != nil {
		fmt.Println("Error generating password:", err)
		return
	}

	fmt.Println("Generated Password:", password)
}
