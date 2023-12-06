/*
 * Crea un programa que sea capaz de generar e imprimir todas las
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso
 */

package main

import (
	"fmt"
)

func main() {
	palabra := "sol"
	permutaciones := generarPermutaciones(palabra)
	for _, perm := range permutaciones {
		fmt.Println(perm)
	}
}

func generarPermutaciones(palabra string) []string {
	var permutaciones []string
	permutacionesRecursivas([]rune(palabra), 0, &permutaciones)
	return permutaciones
}

func permutacionesRecursivas(palabra []rune, inicio int, permutaciones *[]string) {
	if inicio == len(palabra)-1 {
		*permutaciones = append(*permutaciones, string(palabra))
	} else {
		for i := inicio; i < len(palabra); i++ {
			palabra[inicio], palabra[i] = palabra[i], palabra[inicio] // Intercambiamos las letras
			permutacionesRecursivas(palabra, inicio+1, permutaciones) // Llamada recursiva
			palabra[inicio], palabra[i] = palabra[i], palabra[inicio] // Deshacemos el intercambio para la siguiente iteración
		}
	}
}
