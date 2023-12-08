package main

import (
	"bufio"
	"os"
	"strings"
)

func main() {
	dict := map[rune]string{
		'a': "4",
		'b': "I3",
		'c': "[",
		'd': ")",
		'e': "3",
		'f': "|=",
		'g': "&",
		'h': "#",
		'i': "1",
		'j': ",_|",
		'k': "|<",
		'l': "|",
		'm': "[v]",
		'n': "^/",
		'o': "0",
		'p': "?",
		'q': "9",
		'r': "2",
		's': "5",
		't': "7",
		'u': "(_)",
		'v': "\\",
		'w': "N/",
		'x': "><",
		'y': "v/",
		'z': "%",
		' ': " ",
	}

	var result string

	println("Enter text to translate:")
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	input = strings.ToLower(input)

	for _, char := range input {
		if val, ok := dict[char]; ok {
			result += val
		} else {
			result += string(char)
		}
	}

	println(result)
}
