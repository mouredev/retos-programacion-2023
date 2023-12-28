/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

package main

import (
	"fmt"
	"strings"
)

func excelColumnToNumber(columnName string) int {
	// Convertimos el nombre de la columna a mayúsculas para asegurarnos de manejar letras mayúsculas o minúsculas.
	columnName = strings.ToUpper(columnName)

	result := 0
	for _, char := range columnName {
		// Restamos 'A' - 1 para que 'A' sea 1, 'B' sea 2, y así sucesivamente.
		result = result*26 + int(char-'A'+1)
	}

	return result
}

func main() {
	columnName := "CA"
	columnNumber := excelColumnToNumber(columnName)
	fmt.Printf("El número de columna para %s es %d\n", columnName, columnNumber)
}
