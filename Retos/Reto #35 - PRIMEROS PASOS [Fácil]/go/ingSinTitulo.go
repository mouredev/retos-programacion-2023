package main

import (
	"fmt"
)

func main() {
	// Punto 1: Hola, mundo!
	fmt.Println("Hola, mundo!")

	// Punto 2: Crea una variable de texto o string
	miTexto := "¡Hola desde Go!"

	// Punto 3: Crea una variable de número entero
	miEntero := 42

	// Punto 4: Crea una variable de número con decimales
	miDecimal := 3.14

	// Punto 5: Crea una variable de tipo booleano
	miBooleano := true

	// Punto 6: Crea una constante
	const miConstante = 10

	// Punto 7: Usa un if, else if y else
	if miEntero > 50 {
		fmt.Println("El número es mayor que 50")
	} else if miEntero < 50 {
		fmt.Println("El número es menor que 50")
	} else {
		fmt.Println("El número es igual a 50")
	}

	// Punto 8: Crea un Array (slice en Go)
	miArray := []int{1, 2, 3, 4, 5}

	// Punto 9: Crea una lista (slice en Go)
	miLista := []string{"Manzana", "Banana", "Naranja"}

	// Punto 10: Crea una tupla (no aplicable en Go)

	// Punto 11: Crea un set (no aplicable en Go)

	// Punto 12: Crea un diccionario (map en Go)
	miDiccionario := map[string]string{
		"clave1": "valor1",
		"clave2": "valor2",
	}

	// Punto 13: Usa un ciclo for
	for _, elemento := range miArray {
		fmt.Println(elemento)
	}

	// Punto 14: Usa un ciclo foreach (no aplicable en Go)

	// Punto 15: Usa un ciclo while (no es común en Go, se usa for con condición)
	contador := 0
	for contador < 3 {
		fmt.Println("Contador:", contador)
		contador++
	}

	// Punto 16: Crea una función sin parámetros que no retorne nada
	funcionSinParametros()

	// Punto 17: Crea una función con parámetros que no retorne nada
	funcionConParametros(1, "dos")

	// Punto 18: Crea una función con parámetros que retorne valor
	resultado := funcionConRetorno(3, 4)
	fmt.Println("Resultado:", resultado)

	// Punto 19: Crea una clase (no hay clases en Go, se usan estructuras y métodos)
	type Persona struct {
		Nombre string
		Edad   int
	}

	// Punto 20: Muestra control de excepciones (no es común en Go, se usan valores de retorno para errores)
}

// Punto 16: Crea una función sin parámetros que no retorne nada
func funcionSinParametros() {
	fmt.Println("Función sin parámetros")
}

// Punto 17: Crea una función con parámetros que no retorne nada
func funcionConParametros(param1 int, param2 string) {
	fmt.Println("Parámetro 1:", param1)
	fmt.Println("Parámetro 2:", param2)
}

// Punto 18: Crea una función con parámetros que retorne valor
func funcionConRetorno(a, b int) int {
	return a + b
}
