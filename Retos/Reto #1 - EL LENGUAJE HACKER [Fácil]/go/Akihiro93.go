package main

import (
	"fmt"
)

func cambiar_palabras(string1 string) string {
	dict := map[string]string {
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
        "k": "|<",
        "l": "|",
        "m": "[v]",
        "n": "^/",
        "o": "0",
        "p": "?",
        "q": "9",
        "r": "2",
        "s": "5",
        "t": "7",
        "u": "(_)",
        "v": "\\",
        "w": "N/",
        "x": "><",
        "y": "v/",
        "z": "%",
        " ": " ",
	}
	string2 := ""

	for i := 0; i < len(string1); i++{
		palabra := string(string1[i])
		string2 += dict[palabra]
	}
	return string2
}

var palabra string

func main()  {
    fmt.Println("Introduce la palabra:")
    fmt.Scanln(&palabra)
	fmt.Println(cambiar_palabras(palabra))
}