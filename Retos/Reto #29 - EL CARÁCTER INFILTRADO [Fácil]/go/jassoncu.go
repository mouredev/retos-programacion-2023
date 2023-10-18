/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */

package main

import (
	"fmt"
)
 
func findDifferentCharacters(str1, str2 string) []string {
	if len(str1) != len(str2) {
		return nil
	}
 
	differentCharacters := []string{}
 
	for i := 0; i < len(str1); i++ {
		if str1[i] != str2[i] {
			differentCharacters = append(differentCharacters, string(str1[i]))
		}
	}
 
	return differentCharacters
}
 
func main() {
	str1 := "Me llamo-Jasson"
	str2 := "Me llamo Jasson"
 
	result := findDifferentCharacters(str1, str2)
	fmt.Println(result)
 
	str1 = "Me llamo.Jasson Cu"
	str2 = "Me llamo Jasson Cu"
 
	result = findDifferentCharacters(str1, str2)
	fmt.Println(result)
}