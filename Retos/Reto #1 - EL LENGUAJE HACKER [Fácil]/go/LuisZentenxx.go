package main

import (
	"fmt"
	"strings"
)

func main() {
	originalMsg := "Golang reto #1"

	leetCode := map[string]string{
		"a": "4",
		"b": "|3",
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
		"m": "JVI",
		"n": "^/",
		"o": "0",
		"p": "|*",
		"q": "(_,)",
		"r": "I2",
		"s": "5",
		"t": "7",
		"u": "(_)",
		"v": "|/",
		"w": "VV",
		"x": "><",
		"y": "j",
		"z": "2",
	}

	originalMsgLower := strings.ToLower(originalMsg)

	var mensajeLeet strings.Builder
	for _, char := range originalMsgLower {
		charStr := string(char)
		if leetValue, ok := leetCode[charStr]; ok {
			mensajeLeet.WriteString(leetValue)
		} else {
			mensajeLeet.WriteString(charStr)
		}
	}

	fmt.Println("Mensaje codificado en leet:", mensajeLeet.String())
}
