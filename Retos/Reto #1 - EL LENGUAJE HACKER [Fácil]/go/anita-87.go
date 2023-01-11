package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

var dictionary map[string]string = map[string]string{
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

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

func main() {
	fmt.Println("Type the string you want to transform to the hacker language and press enter:")
	reader := bufio.NewReader(os.Stdin)
	msg, err := reader.ReadString('\n')
	if err != nil {
		log.Fatalf("Failed to read the message. Reason: %v", err)
	}
	fmt.Println(translate(msg))
}

func translate(msg string) string {
	translation := ""
	for _, letter := range msg {
		if l, found := dictionary[strings.ToLower(string(letter))]; found {
			translation += l
		} else {
			translation += string(letter)
		}
	}
	return translation
}
