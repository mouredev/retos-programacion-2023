package main

import (
	"fmt"
	"math/rand"
)

var letters = []string{"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
var numbers = []string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
var symbols = []string{"~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|", "\\", ":", ";", "'", "<", ",", ">", ".", "?", "/"}

func main() {

	password := generatePassword(16, true, true, true)
	fmt.Println(password, "\n")

	password = generatePassword(16, true, true, false)
	fmt.Println(password, "\n")

	password = generatePassword(16, true, false, true)
	fmt.Println(password, "\n")

	password = generatePassword(16, true, false, false)
	fmt.Println(password, "\n")

	password = generatePassword(16, false, true, true)
	fmt.Println(password, "\n")

	password = generatePassword(16, false, true, false)
	fmt.Println(password, "\n")

	password = generatePassword(16, false, false, true)
	fmt.Println(password, "\n")
}

func generatePassword(length int, lettersIncluded, numbersIncluded, symbolsIncluded bool) (password string) {

	var passwordType int
	if lettersIncluded {
		passwordType += 4
	}
	if numbersIncluded {
		passwordType += 2
	}

	if symbolsIncluded {
		passwordType += 1
	}

	for i := 0; i < int(length); i++ {
		switch passwordType {
		case 7:
			categoryToSelect := rand.Intn(3)
			switch categoryToSelect {
			case 2:
				getSymbol(password)
			case 1:
				getNumber(password)
			default:
				getChart(password)
			}
		case 6:
			categoryToSelect := rand.Intn(3)
			switch categoryToSelect {
			case 2:
				getChart(password)
			default:
				getNumber(password)
			}
		case 5:
			categoryToSelect := rand.Intn(3)
			switch categoryToSelect {
			case 2:
				getChart(password)
			default:
				getSymbol(password)
			}
		case 4:
			getChart(password)
		case 3:
			categoryToSelect := rand.Intn(2)
			switch categoryToSelect {
			case 1:
				getNumber(password)
			default:
				getSymbol(password)
			}
		case 2:
			getNumber(password)
		default:
			getSymbol(password)
		}
	}
	return
}

func getChart(password string) string {
	chartToSelect := rand.Intn(len(letters))
	password += letters[chartToSelect]
	return password
}

func getNumber(password string) string {
	numberToSelect := rand.Intn(len(numbers))
	password += numbers[numberToSelect]
	return password
}

func getSymbol(password string) string {
	symbolToSelect := rand.Intn(len(symbols))
	password += symbols[symbolToSelect]
	return password
}
