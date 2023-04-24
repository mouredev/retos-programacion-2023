package main

import (
	"fmt"
	"strings"
)

func HackerEncode(textPlain string) string {

	encryptedText := ""
	leetCode := map[string]string{
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
		"0": "o",
		"1": "L",
		"2": "R",
		"3": "E",
		"4": "A",
		"5": "S",
		"6": "b",
		"7": "T",
		"8": "B",
		"9": "g",
	}

	for _, char := range strings.ToLower(textPlain) {
		if leet, ok := leetCode[string(char)]; ok {
			encryptedText += leet
		} else {
			encryptedText += string(char)
		}
	}

	return encryptedText
}

func main() {
	fmt.Println(HackerEncode("leet"))
	fmt.Println(HackerEncode("Mi nombre es Miguelex"))
	fmt.Println(HackerEncode("1234567890"))
	fmt.Println(HackerEncode("Hola Mundo!! Esto es una_prueba con caracteres extrañ@s"))
}
