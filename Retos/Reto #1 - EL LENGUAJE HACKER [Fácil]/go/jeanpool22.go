package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func ConversionLeet(texto string) {
	lowerText := strings.ToLower(texto)
	var leet = map[string]string{
		"a": "4",
		"b": "I3",
		"c": "[",
		"d": ")",
		"e": "3",
		"f": "|=",
		"g": "&",
		"h": "#",
		"i": "1",
		"j": ",_|",
		"k": ">|",
		"l": "1",
		"m": "/\\/\\",
		"n": "^/",
		"o": "0",
		"p": "|*",
		"q": "(_,)",
		"r": "I2",
		"s": "5",
		"t": "7",
		"u": "(_)",
		"v": "\\/",
		"w": "\\/\\/",
		"x": "><",
		"y": "j",
		"z": "2",
	}

	for _, caracter := range lowerText {
		if letra, ok := leet[string(caracter)]; ok {
			fmt.Print(letra)
		} else {
			fmt.Print(string(caracter))
		}
	}
}

func main() {
	fmt.Print("Ingresa el texto que deseas convertir: ")
	reader := bufio.NewReader(os.Stdin)
	texto, _ := reader.ReadString('\n')
	ConversionLeet(texto)
}
