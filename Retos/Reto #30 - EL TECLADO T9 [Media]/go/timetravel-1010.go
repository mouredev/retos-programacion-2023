package main

import (
	"fmt"
	"strings"
)

var keyboard = map[string][]string{
	"1": {",", ".", "?", "!"},
	"2": {"A", "B", "C"},
	"3": {"D", "E", "F"},
	"4": {"G", "H", "I"},
	"5": {"J", "K", "L"},
	"6": {"M", "N", "O"},
	"7": {"P", "Q", "R", "S"},
	"8": {"T", "U", "V"},
	"9": {"W", "X", "Y", "Z"},
	"0": {" "},
}

func read_input(input string) string {
	numbers := strings.Split(input, "-")
	output := ""
	counter := 0

	for _, c := range numbers {
		if len(c) > 1 {
			for _, cc := range c { // Para numeros repetidos.
				counter++
				if counter > len(keyboard[string(cc)]) { // Para evitar error con cosas como 6666
					counter = 1
				}
			}
			counter--
			c = string(c[0])
		}
		output += keyboard[c][counter]
		counter = 0
	}
	return output
}

func main() {
	i := "6-666-88-777-33-3-33-888"
	//i := "6666-666666-88-777-33-0-3-33-888"
	//i := "222222-2222-8888888-0-333333-444444444-77777777-44444"
	fmt.Println(read_input(i))
}
