package main

import (
	"fmt"
	"math/rand"
	"time"
)

func GenerarClave(longitud int, mayusculas bool, numeros bool, caracteresEspeciales bool) string {

	if longitud < 8 || longitud > 16 {
		return "La longitud debe ser mayor a 8 y menor a 16"
	}

	caracteres := "abcdefghijklmnopqrstuvwxyz"

	if mayusculas == true {
		caracteres = caracteres + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	}

	if numeros == true {
		caracteres = caracteres + "1234567890"
	}

	if caracteresEspeciales == true {
		caracteres = caracteres + "~!@#$%^&*()_+`-=[]{}|;':,./<>?"
	}

	rand.Seed(time.Now().UnixNano())
	clave := ""

	for i := 0; i < longitud; i++ {

		clave = clave + string(caracteres[rand.Intn(len(caracteres))])
	}

	return string(clave)
}

func main() {
	fmt.Println(GenerarClave(10, true, true, true))
	fmt.Println(GenerarClave(15, false, true, false))
	fmt.Println(GenerarClave(9, true, true, false))
	fmt.Println(GenerarClave(3, true, true, true))
	fmt.Println(GenerarClave(21, true, true, true))
}
