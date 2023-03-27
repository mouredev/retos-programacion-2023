package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

// Declarar el diccionario como una variable global
var diccionario = map[rune]string{
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
	'k': ">|",
	'l': "1",
	'm': `/\/\`,
	'n': "^/",
	'o': "0",
	'p': "|*",
	'q': "(_,)",
	'r': "I2",
	's': "5",
	't': "7",
	'u': "(_)",
	'v': `\/`,
	'w': `\/\/`,
	'x': "><",
	'y': "j",
	'z': "2",
}

func main() {
	fmt.Println("Introduce el texto a traducir:")
	reader := bufio.NewReader(os.Stdin)
	msg, err := reader.ReadString('\n')

	if err != nil {
		log.Fatal(err)
	}

	msgLower := strings.ToLower(msg)
	var msgTranslate string

	// Recorrer el string y realizar la sustitución
	for _, c := range msgLower {
		sustitucion, existe := diccionario[c]
		if existe {
			msgTranslate += sustitucion
		} else {
			msgTranslate += string(c)
		}
	}

	fmt.Printf("El resultado: %s\n", msgTranslate)
}
