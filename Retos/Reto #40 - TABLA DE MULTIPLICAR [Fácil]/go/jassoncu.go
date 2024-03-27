package main

import (
	"fmt"
)

func main() {
	var numero int

	// Solicitar un número al usuario
	fmt.Print("Ingrese un número para mostrar su tabla de multiplicar: ")
	fmt.Scan(&numero)

	// Imprimir la tabla de multiplicar
	fmt.Printf("Tabla de multiplicar del %d:\n", numero)
	for i := 1; i <= 10; i++ {
		resultado := numero * i
		fmt.Printf("%d x %d = %d\n", numero, i, resultado)
	}
}
