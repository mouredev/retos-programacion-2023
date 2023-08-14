/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */

package main

import (
	"fmt"
	"strings"
)

func T9ToLetters(input string) string {
	t9Mapping := map[rune]string{
		'2': "ABC",
		'3': "DEF",
		'4': "GHI",
		'5': "JKL",
		'6': "MNO",
		'7': "PQRS",
		'8': "TUV",
		'9': "WXYZ",
		'0': " ",
	}

	var result strings.Builder
	prevKey := rune(' ')
	keyCount := 0

	for _, char := range input {
		if char == '-' {
			if keyCount > 0 {
				letters := t9Mapping[prevKey]
				result.WriteString(string(letters[keyCount-1]))
			}
			prevKey = ' '
			keyCount = 0
		} else if val, exists := t9Mapping[char]; exists {
			if prevKey != char {
				if keyCount > 0 {
					letters := t9Mapping[prevKey]
					result.WriteString(string(letters[keyCount-1]))
				}
				prevKey = char
				keyCount = 0
			}
			keyCount = (keyCount + 1) % (len(val) + 1)
		}
	}

	if keyCount > 0 {
		letters := t9Mapping[prevKey]
		result.WriteString(string(letters[keyCount-1]))
	}

	return result.String()
}

func main() {
	input := "6-666-88-777-33-3-33-888"
	output := T9ToLetters(input)
	fmt.Println("Salida:", output) // Debería imprimir "Salida: MOUREDEV"
}
