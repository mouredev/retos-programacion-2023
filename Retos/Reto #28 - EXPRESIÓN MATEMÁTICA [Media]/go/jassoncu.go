/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */

package main

import (
	"fmt"
	"strings"
	"strconv"
)

func esExpresionCorrecta(expresion string) bool {
	// Dividir la expresión en tokens separados por espacios
	tokens := strings.Fields(expresion)

	// Verificar que la cantidad de tokens sea impar (número, operación, número, operación, ...)
	if len(tokens)%2 != 1 {
		return false
	}

	// Iterar sobre los tokens en pasos de 2 para verificar número y operación
	for i := 0; i < len(tokens); i += 2 {
		// Verificar si el token actual es un número válido
		_, err := strconv.ParseFloat(tokens[i], 64)
		if err != nil {
			return false
		}

		// Verificar si hemos llegado al último token
		if i == len(tokens)-1 {
			break
		}

		// Verificar si el token siguiente es una operación válida
		if !esOperacionValida(tokens[i+1]) {
			return false
		}
	}

	return true
}

func esOperacionValida(operacion string) bool {
	operacionesValidas := map[string]bool{
		"+": true,
		"-": true,
		"*": true,
		"/": true,
		"%": true,
	}

	// Verificar si la operación está en el mapa de operaciones válidas
	_, existe := operacionesValidas[operacion]
	return existe
}

func main() {
	expresion := "5 + 6 / 7 - 4"
	fmt.Printf("¿La expresión \"%s\" es correcta? %v\n", expresion, esExpresionCorrecta(expresion))

	expresion = "5 a 6"
	fmt.Printf("¿La expresión \"%s\" es correcta? %v\n", expresion, esExpresionCorrecta(expresion))
}
