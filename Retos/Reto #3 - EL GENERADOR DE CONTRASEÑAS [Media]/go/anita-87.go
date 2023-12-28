package main

import (
	"fmt"
	"math/rand"
	"time"
)

const maxLength = 16
const minLength = 8

var charSet = []rune("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
var numberSet = []rune("0123456789")
var symbolSet = []rune(",.|@#%&()=?¿[]{}_-<>")

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
func main() {
	password := getPassword()
	fmt.Printf(fmt.Sprintf("The password is: %s", password))
}

func getPasswordLength() int {
	rand.Seed(time.Now().UnixNano())
	return rand.Intn(maxLength-minLength) + minLength
}

func getPassword() string {
	length := getPasswordLength()
	str := make([]rune, length)
	for i := 0; i < length; i++ {
		switch getCharsetNumberOrSymbol() {
		case 0:
			str[i] = charSet[rand.Intn(len(charSet))]
		case 1:
			str[i] = numberSet[rand.Intn(len(numberSet))]
		case 2:
			str[i] = symbolSet[rand.Intn(len(symbolSet))]
		}
	}
	return string(str)
}

func getCharsetNumberOrSymbol() int {
	rand.Seed(time.Now().UnixNano())
	return rand.Intn(3 - 0)
}
