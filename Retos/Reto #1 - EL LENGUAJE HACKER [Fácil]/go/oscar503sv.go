package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("*********CONVIERTE TEXTO NORMAL A TEXTO HACKER*********")
	fmt.Println("Introduce un texto: ")
	input, err := reader.ReadString('\n')

	if err != nil {
		fmt.Println("Error al leer el texto")
		return
	}

	fmt.Println(leetTranslator(strings.ToUpper(input)))
}

func leetTranslator(text string) string {
	var alphabet = map[rune]string{'A': "4", 'B': "I3", 'C': "[", 'D': ")", 'E': "3", 'F': "|=", 'G': "&", 'H': "#", 'I': "1", 'J': ",_|", 'K': ">|", 'L': "1", 'M': "JVI", 'N': "^/", 'O': "0", 'P': "|*", 'Q': "(_,)", 'R': "I2", 'S': "5", 'T': "7", 'U': "(_)", 'V': "|/", 'W': "(n)", 'X': "><", 'Y': "j", 'Z': "2"}

	hackerText := ""

	for _, char := range text {
		if replacement, ok := alphabet[char]; ok {
			hackerText += replacement
		} else {
			hackerText += string(char)
		}
	}

	return hackerText
}
