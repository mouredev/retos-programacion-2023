package main

import (
	"fmt"
	"math"
	"sync"
)

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

// Comprobacion para numeros Primo
func esPrimo(num int, validacion *string, wg *sync.WaitGroup) {
	defer wg.Done()

	if num == 0 || num == 1 || num == 4 {
		*validacion = fmt.Sprintf("no es primo")
		return
	}

	for i := 2; i < int(math.Sqrt(float64(num))+1); i++ {
		if num%i == 0 {
			*validacion = fmt.Sprintf("no es primo")
			return
		}
	}
	*validacion = fmt.Sprintf("es primo")

}

// Comprobacion para numeros Pertenecientes a Fibonacci
func esFibonacci(num int, validacion *string, wg *sync.WaitGroup) {
	defer wg.Done()

	if operation1 := math.Sqrt(5*(math.Pow(float64(num), 2)) + 4); (operation1 - math.Round(operation1)) == 0 {
		*validacion = fmt.Sprintf("fibonacci")
		return
	}

	if operation2 := math.Sqrt(5*(math.Pow(float64(num), 2)) - 4); (operation2 - math.Round(operation2)) == 0 {
		*validacion = fmt.Sprintf("fibonacci")
		return
	}

	*validacion = fmt.Sprintf("no es fibonacci")
}

// Comprobacion para numeros Impares
func esImpar(num int, validacion *string, wg *sync.WaitGroup) {
	defer wg.Done()

	if num%2 == 0 {
		*validacion = fmt.Sprintf("es par")
		return
	}
	*validacion = fmt.Sprintf("es impar")
}

func ComprobacionPFI(num int) string {

	var primo string
	var fibonacci string
	var par string

	var wg sync.WaitGroup
	wg.Add(3)
	go esPrimo(num, &primo, &wg)
	go esFibonacci(num, &fibonacci, &wg)
	go esImpar(num, &par, &wg)
	wg.Wait()

	return fmt.Sprintf("%d %s, %s y %s", num, primo, fibonacci, par)
}

func main() {
	fmt.Println(ComprobacionPFI(2))
	fmt.Println(ComprobacionPFI(7))
	fmt.Println(ComprobacionPFI(10))
	fmt.Println(ComprobacionPFI(11))
}
