package main

import (
	"fmt"
	"math/rand"
	"strconv"
)

var input string


func generar_contraseña(t int) {
    // Variables
    letras := "qwertyuiopasdfghjklñzxcvbnm"
    letras_mayusculas := "QWERTYUIOPASDFGHJKLÑZXCVBNM"
    numeros := "1234567890"
    caracteres := "!#$%&/()=.-_,+*;:"
    contraseña := ""

    // Bucle
    for i := 1; i <= t; i++ {
        q := rand.Intn(4)
        if q == 0 {
            n := rand.Intn(len(letras))
            contraseña += string(letras[n])
        }
        if q == 1 {
            n := rand.Intn(len(letras_mayusculas))
            contraseña += string(letras_mayusculas[n])
        }
        if q == 2 {
            n := rand.Intn(len(numeros))
            contraseña += string(numeros[n])
        }
        if q == 3 {
            n := rand.Intn(len(caracteres))
            contraseña += string(caracteres[n])
        }
    }

	fmt.Printf("%s %s", "su contraseña es: ", contraseña )
}

func main()  {
	fmt.Println("Tamaño de la contraseña:")
	fmt.Scanln(&input)
	tamaño, _ := strconv.Atoi(input)
	generar_contraseña(tamaño)
}